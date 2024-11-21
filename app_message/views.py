from django.contrib.auth import authenticate

from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message
from .serializers import MessageSerializers

from app_notification.models import Notification


class CreateMessageView(APIView):
    permission_classes= [permissions.IsAuthenticated]

    def post(self, request):
        request.data['sender_id'] = request.user.user_id  # 
        serializer= MessageSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Message Sent Successfully"},status=status.HTTP_201_CREATED)
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