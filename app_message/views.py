from django.contrib.auth import authenticate

from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message
from .serializers import MessageSerializers
from app_user.models import CustomUser
from app_userprofile.models import UserProfile

from app_notification.models import Notification
from app_notification.serializers import NotificationSerializer
from app_subscription.models import Subscription

#1. Send request

class SendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        sender = request.user
        receiver_id = request.data.get('receiver_id')
        content = request.data.get('content', 'Hi, I would like to connect')


        if not sender.subscription_plan:
            return Response({"error":"You need to subscribe for send request"})

        try:
            receiver = CustomUser.objects.get(user_id=receiver_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "Receiver does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        if sender == receiver:
            return Response({"error": "You cannot send a request to yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure profiles exist
        try:
            sender_profile = UserProfile.objects.get(user_id=sender)
        except UserProfile.DoesNotExist:
            return Response({"error": "Sender profile not found."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            receiver_profile = UserProfile.objects.get(user_id=receiver)
        except UserProfile.DoesNotExist:
            return Response({"error": "Receiver profile not found."}, status=status.HTTP_400_BAD_REQUEST)

        # Restrict sending requests to users with the same gender
        if sender_profile.Gender == receiver_profile.Gender:
            return Response({"error": "You cannot send a request to a user with the same gender."}, status=status.HTTP_400_BAD_REQUEST)

        

        # Check for existing requests
        existing_request = Message.objects.filter(
            sender_id=sender,
            receiver_id=receiver,
            message_type='request'
        ).first()

        if existing_request:
            if existing_request.status == 'pending':
                return Response({"error": "You have already sent a pending request to this user."}, status=status.HTTP_400_BAD_REQUEST)
            elif existing_request.status == 'rejected':
                return Response({"error": "You cannot send another request. The previous request was rejected."}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare message data
        message_data = {
            'sender_id': sender.user_id,
            'receiver_id': receiver.user_id,
            'content': content,
            'message_type': 'request',
            'status': 'pending'
        }

        # Serialize and save the request
        serializer = MessageSerializers(data=message_data)
        if serializer.is_valid():
            serializer.save()

            # Create a notification
            notification_content = f"User with ID {sender.user_id} has sent you a connection request."
            Notification.objects.create(
                receiver=receiver,
                notification_title="New Connection Request",
                notification_content=notification_content,
                status="Pending"
            )
            return Response({"message": "Request sent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#2. Viewing the request

class ViewRequest(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        receiver =  request.user
        messages = Message.objects.filter(receiver_id=receiver, message_type='request',status='pending')
        serializer = MessageSerializers(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#3. Update the request

class UpdateRequestStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        receiver = request.user
        message_id = request.data.get('message_id')
        new_status = request.data.get('status')  # Accepted or Rejected

        # Validate the new status
        if new_status not in ['accepted', 'rejected']:
            return Response({"error": "Invalid status. Choose 'accepted' or 'rejected'."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the message
        try:
            message = Message.objects.get(message_id=message_id, receiver_id=receiver, message_type='request', status='pending')
        except Message.DoesNotExist:
            return Response({"error": "Request not found or already responded to."}, status=status.HTTP_404_NOT_FOUND)

        # Update the status
        message.status = new_status
        message.save()

        # Send a notification to the sender
        notification_content = f"Your connection request to {receiver.username} was {new_status}."
        Notification.objects.create(
            receiver=message.sender_id,
            notification_title="Connection Request Update",
            notification_content=notification_content,
            status="Unread"
        )

        return Response({"message": f"Response {new_status} successfully"}, status=status.HTTP_200_OK)

#1. Create Message 

class CreateMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Get the sender from the authenticated user
        sender = request.user
        receiver_id = request.data.get('receiver_id')  # Receiver ID from the body
        content = request.data.get('content', '')

        # Validate if receiver_id is provided
        if not receiver_id:
            return Response(
                {"error": "Receiver ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Convert receiver_id to an integer and check if the sender is messaging themselves
        try:
            receiver_id = int(receiver_id)
            if sender.user_id == receiver_id:
                return Response(
                    {"error": "You cannot send a message to yourself."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except ValueError:
            return Response(
                {"error": "Invalid Receiver ID. Must be an integer."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validate that the receiver exists
        try:
            receiver = CustomUser.objects.get(user_id=receiver_id)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "Receiver does not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the connection request is accepted
        connection_request = Message.objects.filter(
            sender_id=sender,
            receiver_id=receiver,
            message_type='request',
            status='accepted'
        ).first()

        if not connection_request:
            return Response(
                {"error": "You can only send messages after the connection request is accepted."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create and save the message
        message_data = {
            'sender_id': sender.user_id,  # Derived from the authenticated user
            'receiver_id': receiver.user_id,
            'content': content,
            'message_type': 'message',  # Specify the type for normal messages
            'status': 'unread'
        }

        serializer = MessageSerializers(data=message_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Message Sent Successfully."},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #2. Retrieve all the read message by receiver

#     def get(self, request):
#     # Filter messages where the logged-in user is the recipient
#         messages = Message.objects.filter(receiver_id=request.user,message_type='messages',status='read')
        
#         # Serialize the filtered messages
#         serializer = MessageSerializers(messages, many=True)
        
#         return Response(serializer.data, status=status.HTTP_200_OK)

# Get all unread messages

class UnreadMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        messages=Message.objects.filter(receiver_id=request.user.user_id,status='unread').order_by('-created_on')
        serializer=MessageSerializers(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#3. Message Viewed by receiver

class MessagebyReceiverView(APIView):
    # Ensure the user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # The logged-in user is the receiver
        receiver = request.user  
        # Filter messages where the logged-in user is the receiver
        messages = Message.objects.filter(receiver_id=receiver,message_type='message').order_by('-created_on')
        
        messages.filter(status='unread').update(status='read')
        # Serialize the messages
        Notification.objects.filter(receiver=receiver,status='Unread').update(status='Read')

        serializer = MessageSerializers(messages, many=True)
        
        # Return the serialized messages
        return Response(serializer.data, status=status.HTTP_200_OK)


# Viewing the message history of one user with specific user

class ViewMessageHistory(APIView):
    # Ensure the user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, other_user_id):
        # The logged-in user
        user = request.user

        try:
            # Filter messages sent by the logged-in user to the other user
            sent_messages = Message.objects.filter(
                sender_id=user.user_id,
                receiver_id=other_user_id,
                message_type='message'
            )

            # Filter messages received by the logged-in user from the other user
            received_messages = Message.objects.filter(
                sender_id=other_user_id,
                receiver_id=user.user_id,
                message_type='message'
            )

            # Combine sent and received messages into a single queryset
            messages = sent_messages.union(received_messages).order_by('created_on')

            # Serialize the messages
            serializer = MessageSerializers(messages, many=True)

            # Return the serialized messages
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # Handle any unexpected errors
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )





#4. View new match notification 

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
            return Response({"message": "No match notifications found."}, status=status.HTTP_204_NO_CONTENT)

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

#5. Bulk message viewing by users

class ViewBulkMessages(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Filter notifications with title "Christmas" for the logged-in user
        notifications = Notification.objects.filter(
            receiver_id=request.user.user_id,
            notification_title="New year greetings"  # Change this to the actual title you want to match
        ).order_by('-created_on')

        if not notifications.exists():
            return Response({"message": "No bulk notifications found."}, status=status.HTTP_204_NO_CONTENT)

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


#6. viewing the master table changes notification

class ViewMasterTableNotification(APIView):
    permission_classes=[permissions.IsAuthenticated]


    def get(self, request):
        # Get the logged-in user
        user = request.user

        # Get the notifications related to changes in the MasterTable for the logged-in user
        notifications = Notification.objects.filter(
            receiver_id=user.user_id,
            #It is used to check whether a given title exists in a field's value, ignoring case differences.
            notification_title__icontains="Value Added"  # Filter by notification title
        ).order_by('-created_on')

        if not notifications.exists():
            return Response({"message": "No MasterTable change notifications found."}, status=status.HTTP_204_NO_CONTENT)

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


#7. Viewing the reminder notification

class ViewRemindernotification(APIView):
    permission_classes =  [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user

        notifications = Notification.objects.filter(
            receiver_id=user.user_id,
            notification_title__icontains="Reminder"  # Filter by notification title
        ).order_by('-created_on')

        if not notifications.exists():
            return Response({"message": "No Reminder notifications found."}, status=status.HTTP_204_NO_CONTENT)

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

#8. Viewing the new subscription notification

class NewSubscriptionNotificationsView(APIView):
    """
    API View for users to view notifications about new subscription plans and mark them as read.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Fetch notifications for the logged-in user about new subscription plans
        user = request.user
        notifications = Notification.objects.filter(
            receiver_id=user.user_id,
            notification_title__icontains="New Subscription Plan",
            status="Unread"  # Fetch only unread notifications
        ).order_by('-created_on')

        if not notifications.exists():
            return Response({"message": "No new notifications about subscription plans."}, status=status.HTTP_200_OK)

        # Serialize the filtered notifications
        notification_data = [
            {
                "id": notification.notification_id,
                "title": notification.notification_title,
                "content": notification.notification_content,
                "status": notification.status,
                "created_on": notification.created_on,
            }
            for notification in notifications
        ]

        # Mark all fetched notifications as "Read"
        notifications.update(status="Read")

        return Response({"notifications": notification_data}, status=status.HTTP_200_OK)