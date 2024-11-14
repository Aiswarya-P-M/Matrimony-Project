from rest_framework import serializers
from .models import Matching
from app_userprofile.serializers import UserProfileSerializer


class MatchingSerializer(serializers.ModelSerializer):
    user1 = UserProfileSerializer()
    user2 = UserProfileSerializer()
    
    class Meta:
        model = Matching
        fields = ['user1', 'user2', 'status', 'match_score']  # Adjust fields as needed