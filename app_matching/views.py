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

    def get(self, request):
        # Extract user1_id and user2_id from the request data
        user1_id = request.data.get("user1_id")
        user2_id = request.data.get("user2_id")

        # Validate that user1_id and user2_id are provided
        if not user1_id or not user2_id:
            return Response(
                {"error": "Both user1_id and user2_id are required."},
                status=400
            )

        # Ensure the token belongs to user1
        if request.user.user_id != user1_id:
            return Response(
                {"error": "You are not authorized to perform this action for the specified user1_id."},
                status=403
            )

        # Ensure user1 and user2 are not the same
        # if user1_id == user2_id:
        #     return Response(
        #         {"error": "Cannot match the same user. Please select a different profile."},
        #         status=400
        #     )

        # Get user1 and user2
        user1 = get_object_or_404(CustomUser, user_id=user1_id)
        user2 = get_object_or_404(CustomUser, user_id=user2_id)

        # Get user profiles and preferences
        try:
            user1_profile = UserProfile.objects.get(user_id=user1.user_id)
            user2_profile = UserProfile.objects.get(user_id=user2.user_id)
            user1_preference = Preference.objects.get(user_id=user1.user_id)
            user2_preference = Preference.objects.get(user_id=user2.user_id)
        except UserProfile.DoesNotExist:
            return Response({"error": f"Profile not found for user {user1.username} or {user2.username}."}, status=404)
        except Preference.DoesNotExist:
            return Response({"error": f"Preference not found for user {user1.username} or {user2.username}."}, status=404)

        # Calculate match score
        match_score = calculate_match_score(user1_preference, user2_profile)

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
        }, status=201)
