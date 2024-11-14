from django.shortcuts import render
from django.http import JsonResponse
from app_preference.models import Preference
from app_userprofile.models import UserProfile
from app_user.models import CustomUser
from .models import Matching
from .utils import calculate_match_score  # <-- Import the utility function
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response


class FindMatchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user2_id):
        user1 = request.user
        
        # Debugging statements to verify distinct user values
        print("Debug - user1 ID:", user1.user_id)
        print("Debug - user2_id:", user2_id)
        
        # Ensure user1 and user2 are not the same
        if user1.user_id == user2_id:
            return Response(
                {"error": "Cannot match the same user. Please select a different profile."},
                status=400
            )
        
        # Get user2 as a distinct CustomUser instance
        user2 = get_object_or_404(CustomUser, user_id=user2_id)
        
        # Get user profiles and preferences
        user1_profile = UserProfile.objects.get(user_id=user1.user_id)
        user2_profile = UserProfile.objects.get(user_id=user2.user_id)
        user1_preference = Preference.objects.get(user_id=user1.user_id)
        user2_preference = Preference.objects.get(user_id=user2.user_id)
        
        # Calculate match score
        match_score = calculate_match_score(user1_profile, user2_preference)
        
        # Set match status based on score
        status = 'accepted' if match_score >= 70 else 'pending'
        
        # Create match record
        match = Matching.objects.create(
            user1=user1, 
            user2=user2, 
            status=status, 
            match_score=match_score
        )
        
        return Response({
            'user1': user1.username,
            'user2': user2.username,
            'match_score': match_score,
            'status': status
        })
