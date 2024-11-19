from django.db import models
from app_user.models import CustomUser
# Create your models here.

class Message(models.Model):
    STATUS_CHOICES = [
        ('read','Read'),
        ('unread', 'Unread'),
    ]
    message_id=models.AutoField(primary_key=True)
    sender_id=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='sender')
    receiver_id=models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='receiver')
    content=models.TextField()
    status=models.CharField(max_length=10, choices=STATUS_CHOICES,default='unread')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    received_at = models.DateTimeField(auto_now_add=True)

