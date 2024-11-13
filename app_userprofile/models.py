from django.db import models
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


    