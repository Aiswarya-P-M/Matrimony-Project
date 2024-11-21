
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *

class CustomUserserializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_id","username","email","password","phone_number","first_name","last_name","joined_date","last_login",
        "subscription_plan","is_active","role"]

    
    def validate_password(self, value):
        try:
            # Validate the password using Django's password validators
            validate_password(value)
        except ValidationError as e:
            # Return a readable error message
            raise serializers.ValidationError({"password": e.messages})
        return value
    