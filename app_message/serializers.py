from rest_framework import serializers
from .models import Message

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=['message_id','sender_id','receiver_id','content','message_type','status']
