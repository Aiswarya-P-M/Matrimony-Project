from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField
from app_subscription.models import Subscription


class CustomUser(AbstractUser):
    # Define the role choices
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'Normal User'
        SUSPENDED = 'suspended', 'Suspended User'

    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone_number=PhoneNumberField(unique=True,null=True,blank=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    joined_date=models.DateField(auto_now_add=True)
    last_login=models.DateField(auto_now=True)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)
    is_active=models.BooleanField(default=True)
    subscription_plan=models.ForeignKey(Subscription,on_delete=models.DO_NOTHING, null=True, blank=True)
    is_superuser=models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.USER  # Default to 'user' role
    )
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    # objects = CustomUserManager()
    def save(self, *args, **kwargs):
        if self.password:  # Ensure password is hashed only if set
            self.set_password(self.password)
        super().save(*args, **kwargs)