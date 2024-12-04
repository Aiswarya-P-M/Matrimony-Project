from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date

from app_user.models import CustomUser
# Create your models here.
class UserProfile(models.Model):
    user_id=models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING,null=True,blank=True)
    Gender=models.CharField(max_length=50, null=True, blank=True)
    Date_of_Birth=models.DateField(null=True, blank=True)
    Age=models.IntegerField(null=True, blank=True)
    Height=models.IntegerField(null=True, blank=True)
    Weight=models.IntegerField(null=True, blank=True)
    Religion=models.CharField(max_length=50, null=True, blank=True)
    Caste=models.CharField(max_length=50, null=True, blank=True)
    Income=models.IntegerField(null=True, blank=True)
    Profession=models.CharField(max_length=50, null=True, blank=True)
    Education=models.CharField(max_length=50, null=True, blank=True)
    Bio=models.CharField(max_length=500, null=True, blank=True)
    Marital_status=models.CharField(max_length=30,null=True,blank=True)
    Location=models.CharField(max_length=200, null=True, blank=True)
    Language=models.CharField(max_length=50, null=True, blank=True)
    Profile_img=models.ImageField(upload_to='profile_img')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.Date_of_Birth:
            # Validate if Date_of_Birth is not in the future
            # if self.Date_of_Birth > timezone.now().date():
            #     raise ValidationError("Date of birth cannot be in the future.")

            today = timezone.now().date()
            self.Age = today.year - self.Date_of_Birth.year - (
                (today.month, today.day) < (self.Date_of_Birth.month, self.Date_of_Birth.day)
            )
        
        super().save(*args, **kwargs)


    

    def __str__(self):
        return f"Profile of {self.user_id.username}"