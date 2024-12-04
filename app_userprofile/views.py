from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .models import UserProfile
from .serializers import UserProfileserializers

# 1. creating a profile

class CreateProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        # Check if a profile already exists for the user
        if UserProfile.objects.filter(user_id=request.user).exists():
            return Response({"message": "A profile already exists for this user."}, status=status.HTTP_400_BAD_REQUEST)

        # If no profile exists, proceed to create a new one
        serializer = UserProfileserializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)  # Associate the profile with the current user
            return Response({"message": "Profile created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
# 2. Viewing the details of all profile

    def get(self, request):
        profile=UserProfile.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Or use PAGE_SIZE from settings.py
        paginated_profile = paginator.paginate_queryset(profile, request)
        serializer=UserProfileserializers(paginated_profile, many=True)
        return paginator.get_paginated_response(serializer.data)


#3. get profile details of specific user

class ProfileDetailsView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request):
        try:
            # Use user_id instead of id
            profile = UserProfile.objects.get(user_id=request.user.user_id)
            serializer = UserProfileserializers(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({"message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

#4. Update Profile details

    def put(self, request):
        try:
            # Use user_id instead of id
            profile = UserProfile.objects.get(user_id=request.user.user_id)
            serializer = UserProfileserializers(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserProfile.DoesNotExist:
            return Response({"message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

#5. Delete Profile
    def delete(self,request,user_id):
        try:
            profile=UserProfile.objects.get(user_id=user_id)
            profile.is_active=False
            profile.save()
            return Response({"Message":"Profile deleted successfully"},status=status.HTTP_200_OK)
        except:
            return Response({"message":"Profile not found"},status=status.HTTP_400_BAD_REQUEST) 