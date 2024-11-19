from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from app_preference.models import Preference
from app_userprofile.models import UserProfile
from app_user.models import CustomUser
from .models import Matching
from .utils import calculate_match_score  # <-- Import the utility function


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

class FindAllMatchesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get the logged-in user
        user = request.user
        try:
            user_profile = UserProfile.objects.get(user_id=user.user_id)
            user_preference = Preference.objects.get(user_id=user.user_id)
        except (UserProfile.DoesNotExist, Preference.DoesNotExist):
            return Response({"error": "User profile or preferences not found."}, status=status.HTTP_404_NOT_FOUND)

        # List to store match results
        match_results = []

        # Loop through all users (excluding the logged-in user)
        all_users = CustomUser.objects.all()
        for other_user in all_users:
            if other_user.user_id == user.user_id:  # Skip the logged-in user
                continue

            try:
                other_user_profile = UserProfile.objects.get(user_id=other_user.user_id)
                match_score = calculate_match_score(user_preference, other_user_profile)
                
                if match_score > 0:  # Only include matches with a positive score
                    # Set status based on match score
                    status_value = 'accepted' if match_score >= 70 else 'pending'

                    match_results.append({
                        'user1_id': user.user_id,
                        'user2_id': other_user.user_id,
                        'match_score': match_score,
                        'status': status_value
                    })
            except UserProfile.DoesNotExist:
                continue  # Skip users without profiles

        # Sorting match results manually
        for i in range(len(match_results)):
            for j in range(i + 1, len(match_results)):
                if match_results[i]['match_score'] < match_results[j]['match_score']:
                    # Swap the elements if the current score is less than the next one
                    match_results[i], match_results[j] = match_results[j], match_results[i]

        return Response(match_results, status=status.HTTP_200_OK)  