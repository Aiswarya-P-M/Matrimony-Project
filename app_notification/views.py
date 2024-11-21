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

# class MatchNotificationView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self,request):
#         if not(request.user.is_admin and request.user.is_staff and request.user.is_superuser):
#             return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

#             user_id = request.data.get("user_id")
#             user = Customuser.objects.get(id=user_id)