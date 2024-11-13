from django.db import models
from app_user.models import CustomUser
from app_commonmatching.models import CommonMatchingTable,MasterTable
# Create your models here.
class Preference(models.Model):
    user_id = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True)
    Age=models.IntegerField(null=True, blank=True)
    Profession=models.CharField(max_length=100, null=True, blank=True)
    Education=models.CharField(max_length=100, null=True, blank=True)
    Location=models.CharField(max_length=100, null=True, blank=True)
    Caste=models.CharField(max_length=50, null=True, blank=True)
    Religion=models.CharField(max_length=50, null=True, blank=True)
    Income=models.IntegerField(null=True, blank=True)
    Height=models.IntegerField(null=True, blank=True)
    Weight=models.IntegerField(null=True, blank=True)
    Gender=models.CharField(max_length=50, null=True, blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    