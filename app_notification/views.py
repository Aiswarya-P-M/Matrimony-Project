# from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
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
from app_commonmatching.models import CommonMatchingTable, MasterTable

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
        active_users = CustomUser.objects.filter(is_active=True,is_admin=False)

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

class AddMasterTableEntryAndNotify(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Check if the user has the necessary permissions (admin, staff, superuser)
        if not (request.user.is_admin and request.user.is_staff and request.user.is_superuser):
            return Response({"error": "You do not have permission to do this action."}, status=status.HTTP_403_FORBIDDEN)

        # Get the type_id and value from the request data
        type_id = request.data.get('type_id')
        value = request.data.get('value')
        print(type_id, value)

        # Check if both type_id and value are provided
        if not type_id or not value:  # Corrected the condition
            return Response({"error": "Both type_id and value are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the CommonMatchingTable entry using type_id
            common_type = CommonMatchingTable.objects.get(type_id=type_id)
        except CommonMatchingTable.DoesNotExist:
            return Response({"error": "Invalid type_id."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the new MasterTable entry, passing the primary key (type_id) from common_type
        new_entry = MasterTable.objects.create(type=common_type, value=value)

        # Get all active users
        users = CustomUser.objects.filter(is_active=True,is_admin=False)
        notification_message = f"A new value has been added to {common_type.type}: {value}."

        # Create notifications for each active user
        for user in users:
            Notification.objects.create(
                receiver_id=user.user_id,  # Assuming receiver_id is the user_id of CustomUser
                notification_title=f"New {common_type.type} Value Added",
                notification_content=notification_message,
                status="Unread"  # Mark as unread initially
            )

        return Response(
            {"message": f"New {common_type.type} value '{value}' added successfully and notifications sent."},
            status=status.HTTP_201_CREATED
        )




# Reminder to users whose subscription will expire within 2 days.

class NotifyExpiringSubscriptionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Check if the user has the necessary permissions (admin, staff, superuser)
        if not (request.user.is_admin and request.user.is_staff and request.user.is_superuser):
            return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

        # Calculate the date 2 days from now
        notification_date = datetime.now().date() + timedelta(days=2)

        # Fetch users whose subscription plans are expiring in 2 days
        expiring_users = CustomUser.objects.filter(
            is_active=True, 
            subscription_plan__end_date=notification_date,
            subscription_plan__status='active'
        )

        # If no users are found, return a message
        if not expiring_users.exists():
            return Response({"message": "No subscriptions expiring within the next 2 days."}, status=status.HTTP_200_OK)

        # Send notifications to each user
        for user in expiring_users:
            notification_message = (
                f"Your subscription plan '{user.subscription_plan.plan_type}' will expire on {user.subscription_plan.end_date}. "
                "Please renew to continue enjoying our services."
            )
            Notification.objects.create(
                receiver_id=user.user_id,  # Assuming Notification model has receiver_id
                notification_title="Subscription Expiry Reminder",
                notification_content=notification_message,
                status="Unread"
            )

        return Response(
            {"message": f"Notifications sent to {expiring_users.count()} user(s) with expiring subscriptions."},
            status=status.HTTP_200_OK
        )