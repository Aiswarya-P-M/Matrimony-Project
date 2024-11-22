from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Notification
from .serializers import NotificationSerializer

from app_message.models import Message
from app_message.serializers import MessageSerializers
from app_user.models import CustomUser
from app_subscription.models import Subscription
from app_userprofile.models import UserProfile
from app_preference.models import Preference


#1. Unread message notification

class UnreadMessageNotificationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        # Check if the request is made by an admin
        if not (request.user.is_admin and request.user.is_staff and request.user.is_superuser):
            return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

        # Fetch unread messages for the given user
        unread_messages = Message.objects.filter(
            receiver_id=user_id,
            status__iexact='unread'  # Case-insensitive match for 'status'
        ).order_by('-created_on')
        unread_count = unread_messages.count()

        # Create a notification if there are unread messages
        if unread_count > 0:
            notification_message = f"You have {unread_count} unread messages."
            Notification.objects.create(
                receiver_id=user_id,
                notification_title="Unread Messages Alert",
                notification_content=notification_message,
                status="Unread"
            )
        else:
            notification_message = "No unread messages."

        # Serialize the unread messages
        serializer = MessageSerializers(unread_messages, many=True)
        return Response(
            {
                "unread_count": unread_count,
                "unread_messages": serializer.data,
                "notification": notification_message
            },
            status=status.HTTP_200_OK
        )


#2. Matchfound Notification when creating anew profile(only for users with subscription plan premium and platinum)

class NewMatchNotificationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Ensure the user is an admin
        if not (request.user.is_admin and request.user.is_staff and request.user.is_superuser):
            return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

        # Get the latest profile created
        latest_profile = UserProfile.objects.order_by('-created_on').first()
        if not latest_profile:
            return Response({"error": "No profile found."}, status=status.HTTP_204_NO_CONTENT)

        # Get the new profile's user_id and gender
        new_profile_user_id = latest_profile.user_id.user_id
        new_profile_gender = latest_profile.Gender

        if not new_profile_gender:
            return Response({"error": "The new profile does not have a specified gender."}, status=status.HTTP_400_BAD_REQUEST)

        # Get all eligible users with a premium or platinum subscription
        eligible_users = CustomUser.objects.filter(subscription_plan__plan_type__in=['premium', 'platinum'], is_active=True)

        # Filter eligible users based on preference gender
        matched_users = []
        for user in eligible_users:
            try:
                # Get the user's preference
                preference = Preference.objects.get(user_id=user.user_id)
                if preference.Gender == new_profile_gender:  # Match based on preference gender
                    matched_users.append(user)
            except Preference.DoesNotExist:
                continue  # Skip users without preferences

        if not matched_users:
            return Response({"error": "No users found whose preferences match the new profile's gender."}, status=status.HTTP_404_NOT_FOUND)

        # Create the notification message with the new profile's user_id
        notification_message = f"Congratulations! A new match has been found: User ID {new_profile_user_id}."

        # Create a notification for each matched user
        for user in matched_users:
            Notification.objects.create(
                receiver_id=user.user_id,  # Send notification to the matched user
                notification_title="New Match Found",
                notification_content=notification_message,
                status="Unread"  # Mark it as unread initially
            )

        return Response({"message": "Notifications sent successfully to all matched users."}, status=status.HTTP_201_CREATED)



# bulk message notification

class BulkMessageNotificationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Ensure the user is an admin
        if not (request.user.is_admin and request.user.is_staff and request.user.is_superuser):
            return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

        # Get the festival name and message from the request
        message_title = request.data.get("message_title")
        message_content = request.data.get("message_content")

        if not message_title or not message_content:
            return Response({"error": "message_title and message_content are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Get all active users
        active_users = CustomUser.objects.filter(is_active=True)

        if not active_users.exists():
            return Response({"error": "No active users found."}, status=status.HTTP_404_NOT_FOUND)

        # Create a notification for each active user
        for user in active_users:
            Notification.objects.create(
                receiver_id=user.user_id,
                notification_title=message_title,
                notification_content=message_content,
                status="Unread"  # Mark it as unread initially
            )

        return Response({"message": f"{message_title} message sent successfully to all active users."}, status=status.HTTP_201_CREATED)


# Get notification to users while admin made any changes in the master table

# class NewFeatureAddedView(APIView):