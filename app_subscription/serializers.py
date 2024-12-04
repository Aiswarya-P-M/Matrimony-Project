from rest_framework import serializers
from .models import Subscription
from app_user.models import CustomUser

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subscription
        fields='__all__'

class CustomUserSubscriptionSerializer(serializers.ModelSerializer):
    subscription_plan = SubscriptionSerializer()
    class Meta:
        model = CustomUser
        fields = fields = ['user_id', 'username', 'email', 'phone_number', 'is_active', 'subscription_plan']  # Include all required fields