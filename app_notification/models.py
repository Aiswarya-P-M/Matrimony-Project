from django.db import models
from app_user.models import CustomUser
# Create your models here.

class Notification(models.Model):
    notification_id=models.AutoField(primary_key=True)
    notification_title = models.CharField(max_length=300)
    notification_content = models.TextField()
    receiver = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='notification_receiver',null=True,blank=True)
    status = models.CharField(max_length=20, choices=[
        ('Unread', 'Unread'),
        ('Read', 'Read')
    ])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

