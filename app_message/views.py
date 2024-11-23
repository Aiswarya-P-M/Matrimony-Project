from django.contrib.auth import authenticate

from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message
from .serializers import MessageSerializers

from app_notification.models import Notification
from app_notification.serializers import NotificationSerializer

class CreateMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Get the sender (authenticated user) and their subscription plan
        sender = request.user
        subscription = sender.subscription_plan

        # Set message limits based on the subscription plan
        if subscription:
            if subscription.plan_type == 'basic':
                message_limit = 10
            elif subscription.plan_type == 'premium':
                message_limit = 40
            elif subscription.plan_type == 'platinum':
                message_limit = None  # Unlimited messages
            else:
                message_limit = 0  # Default to no messages for invalid plans
        else:
            return Response(
                {"error": "You need a subscription to send messages."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Count messages sent by the user
        sent_messages_count = Message.objects.filter(sender_id=sender.user_id).count()

        # Check if the user has exceeded their message limit
        if message_limit is not None and sent_messages_count >= message_limit:
            return Response(
                {"error": f"You have reached your message limit of {message_limit} for your subscription plan."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Set sender_id in the request data and validate the serializer
        request.data['sender_id'] = sender.user_id
        serializer = MessageSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Message Sent Successfully"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self,request):
        messages = Message.objects.all()
        serializer = MessageSerializers(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MessagebyReceiverView(APIView):
    # Ensure the user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # The logged-in user is the receiver
        receiver = request.user  
        # Filter messages where the logged-in user is the receiver
        messages = Message.objects.filter(receiver_id=receiver).order_by('-created_on')
        
        messages.filter(status='unread').update(status='read')
        # Serialize the messages
        Notification.objects.filter(receiver=receiver,status='Unread').update(status='Read')

        serializer = MessageSerializers(messages, many=True)
        
        # Return the serialized messages
        return Response(serializer.data, status=status.HTTP_200_OK)

    


class UnreadMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        messages=Message.objects.filter(sender_id=request.user,status='unread').order_by('-created_on')
        serializer=MessageSerializers(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ViewMatchNotification(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get the logged-in user
        user = request.user

        # Retrieve match notifications for the logged-in user
        notifications = Notification.objects.filter(
            receiver_id=user.user_id, 
            notification_title="New Match Found"
        ).order_by('-created_on')

        if not notifications.exists():
            return Response({"message": "No match notifications found."}, status=status.HTTP_404_NOT_FOUND)

        # Update unread notifications to read
        notifications.filter(status="Unread").update(status="Read")

        # Serialize the notifications
        serialized_notifications = [
            {
                "id": notification.notification_id,
                "title": notification.notification_title,
                "content": notification.notification_content,
                "status": notification.status,
                "created_on": notification.created_on,
            }
            for notification in notifications
        ]

        return Response(
            {"match_notifications": serialized_notifications},
            status=status.HTTP_200_OK
        )

# Bulk message viewing by users

class ViewBulkMessages(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Filter notifications with title "Christmas" for the logged-in user
        notifications = Notification.objects.filter(
            receiver_id=request.user.user_id,
            notification_title="Christmas"  # Change this to the actual title you want to match
        ).order_by('-created_on')

        if not notifications.exists():
            return Response({"message": "No bulk notifications found."}, status=status.HTTP_404_NOT_FOUND)

        # Mark notifications as "Read"
        notifications.filter(status="Unread").update(status="Read")

        # Serialize and return the notifications
        serialized_notifications = [
            {
                "id": notification.notification_id,
                "title": notification.notification_title,
                "content": notification.notification_content,
                "status": notification.status,
                "created_on": notification.created_on,
            }
            for notification in notifications
        ]

        return Response(
            {"message_notifications": serialized_notifications},
            status=status.HTTP_200_OK
        )


# viewing the master table changes notification
class ViewMasterTableNotification(APIView):
    permission_classes=[permissions.IsAuthenticated]


    def get(self, request):
        # Get the logged-in user
        user = request.user

        # Get the notifications related to changes in the MasterTable for the logged-in user
        notifications = Notification.objects.filter(
            receiver_id=user.user_id,
            notification_title__icontains="Value Added"  # Filter by notification title
        ).order_by('-created_on')

        if not notifications.exists():
            return Response({"message": "No MasterTable change notifications found."}, status=status.HTTP_404_NOT_FOUND)

        # Mark notifications as "Read" by updating their status
        notifications.filter(status="Unread").update(status="Read")

        # Serialize the notifications
        serialized_notifications = [
            {
                "id": notification.notification_id,
                "title": notification.notification_title,
                "content": notification.notification_content,
                "status": notification.status,
                "created_on": notification.created_on,
            }
            for notification in notifications
        ]

        return Response(
            {"notifications": serialized_notifications},
            status=status.HTTP_200_OK
        )

class ViewRemindernotification(APIView):
    permission_classes =  [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user

        notifications = Notification.objects.filter(
            receiver_id=user.user_id,
            notification_title__icontains="Reminder"  # Filter by notification title
        ).order_by('-created_on')

        if not notifications.exists():
            return Response({"message": "No Reminder notifications found."}, status=status.HTTP_404_NOT_FOUND)

        # Mark notifications as "Read" by updating their status
        notifications.filter(status="Unread").update(status="Read")

        # Serialize the notifications
        serialized_notifications = [
            {
                "id": notification.notification_id,
                "title": notification.notification_title,
                "content": notification.notification_content,
                "status": notification.status,
                "created_on": notification.created_on,
            }
            for notification in notifications
        ]

        return Response(
            {"notifications": serialized_notifications},
            status=status.HTTP_200_OK
        )