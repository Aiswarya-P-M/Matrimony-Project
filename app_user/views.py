from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import  make_password
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserserializers
from rest_framework import permissions
# Create your views here.


class UsercreateView(APIView):
    def post(self,request):
        serializer=CustomUserserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Created Successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        user=CustomUser.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Or use PAGE_SIZE from settings.py
        paginated_users = paginator.paginate_queryset(user, request)
        
        serializer = CustomUserserializers(paginated_users, many=True)
        return paginator.get_paginated_response(serializer.data)

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Pass the raw password to authenticate, not a manually hashed one
        user = authenticate(username=username, password=password)
        
        if user is not None and user.is_active:
            # Get or create token for the authenticated user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({'message':'Logout Successfully'},status=status.HTTP_200_OK)

class UserdetailsView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request):
        user = request.user  # Get the authenticated user from the token
        serializer = CustomUserserializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user  # Get the authenticated user from the token

        # Optional: prevent updates if the user is inactive
        if not user.is_active:
            return Response({'error': 'User is inactive and cannot be updated.'}, status=status.HTTP_403_FORBIDDEN)

        # Allow partial updates with `partial=True`
        serializer = CustomUserserializers(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeactivateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):
        user = request.user  # Get the authenticated user from the token

        if not user.is_active:
            return Response({'message': 'User is already deactivated'}, status=status.HTTP_400_BAD_REQUEST)

        # Set is_active to False instead of deleting the user
        user.is_active = False
        user.save()

        # Respond with a success message indicating the user has been deactivated
        return Response({'message': f'User {user.username} deactivated successfully'}, status=status.HTTP_200_OK)