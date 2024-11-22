from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404

from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import CustomUserserializers

from app_userprofile.models import UserProfile
from app_preference.models import Preference
# Create your views here.

#users

#1. User creation

class UsercreateView(APIView):
    def post(self,request):
        serializer=CustomUserserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User Created Successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self,request):
    #     user=CustomUser.objects.all()
    #     paginator = PageNumberPagination()
    #     paginator.page_size = 2  # Or use PAGE_SIZE from settings.py
    #     paginated_users = paginator.paginate_queryset(user, request)
        
    #     serializer = CustomUserserializers(paginated_users, many=True)
    #     return paginator.get_paginated_response(serializer.data)

#2. Login

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # print(username,password)
        # Pass the raw password to authenticate, not a manually hashed one
        user = authenticate(username=username, password=password)
        # print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{user}")
        if user is not None and user.is_active:
            # Get or create token for the authenticated user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#3. Logout

class UserLogoutView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({'message':'Logout Successfully'},status=status.HTTP_200_OK)

#4. get user details by id

class UserdetailsView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request):
        user = request.user  # Get the authenticated user from the token
        serializer = CustomUserserializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

#5. update user details

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

#6. Deactivate user 

class UserDeactivateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):
        user = request.user  # Get the authenticated user from the token

        if not user.is_active:
            return Response({'message': 'User is already deactivated'}, status=status.HTTP_400_BAD_REQUEST)

        # Set is_active to False instead of deleting the user
        user.is_active = False
        user.save()

        UserProfile.objects.filter(user_id=user).update(is_active=False)

        # Deactivate Preference
        Preference.objects.filter(user_id=user).update(is_active=False)

        # Respond with a success message
        return Response(
            {'message': f'User {user.username}, profile, and preferences deactivated successfully'},
            status=status.HTTP_200_OK
        )

#7. Resetpassword

class ResetPasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = request.user
        username =  request.data.get('username')
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if username != user.username:
            return Response(
                {"message": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )

        if not old_password or not new_password:
            return Response({"message": "Old and new passwords are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(old_password):
            return Response({"message": "Incorrect old password."},
                            status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({"message": "Password reset successfully."}, status=status.HTTP_200_OK)


# Admin

#1. Admin can view all the user details


class UserListView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        # Check if the user is an admin by checking is_admin, is_staff, or is_superuser
        if not (request.user.is_admin or request.user.is_staff or request.user.is_superuser):
            return Response({"error": "You do not have permission to view this data."}, status=403)

        # Get all users
        users = CustomUser.objects.filter(is_admin=False, is_staff=False, is_superuser=False)
        
        # Paginate the users
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Or use PAGE_SIZE from settings.py
        paginated_users = paginator.paginate_queryset(users, request)
        
        # Serialize the users data
        serializer = CustomUserserializers(paginated_users, many=True)
        
        # Remove password field before sending response
        for user_data in serializer.data:
            if 'password' in user_data:
                user_data.pop('password')  # Remove the password from the response

        return paginator.get_paginated_response(serializer.data)


class DeactivateUserbyAdminView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self,request,user_id):
        admin_user = request.user

        # Check if the logged-in user is an admin
        if not (admin_user.is_admin and admin_user.is_staff and admin_user.is_superuser):
            return Response(
                {'message': 'You do not have the necessary permissions to deactivate a user.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Get the user to be deactivated
        user = get_object_or_404(CustomUser, user_id=user_id)

        if not user.is_active:
            return Response({'message': f'User {user.username} is already deactivated.'}, status=status.HTTP_400_BAD_REQUEST)

        # Deactivate the user using update
        CustomUser.objects.filter(user_id=user_id).update(is_active=False,role='suspended')
        UserProfile.objects.filter(user_id=user_id).update(is_active=False)
        Preference.objects.filter(user_id=user_id).update(is_active=False)

        return Response({'message': f'User {user.username} deactivated successfully.'}, status=status.HTTP_200_OK)


class ActiveUsersListView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        # Check if the user is an admin by checking is_admin, is_staff, or is_superuser
        if not (request.user.is_admin or request.user.is_staff or request.user.is_superuser):
            return Response({"error": "You do not have permission to view this data."}, status=403)

        # Get all users
        users = CustomUser.objects.filter(is_admin=False, is_staff=False, is_superuser=False,is_active=True)
        
        # Paginate the users
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Or use PAGE_SIZE from settings.py
        paginated_users = paginator.paginate_queryset(users, request)
        
        # Serialize the users data
        serializer = CustomUserserializers(paginated_users, many=True)
        
        # Remove password field before sending response
        for user_data in serializer.data:
            if 'password' in user_data:
                user_data.pop('password')  # Remove the password from the response

        return paginator.get_paginated_response(serializer.data)


class InactiveUsersListView(APIView):
    def get(self,request):
        # if not (request.user.is_admin or request.user.is_staff or request.user.is_superuser):
        #     return Response({"error": "You do not have permission to view this data."}, status=403)

        users=CustomUser.objects.filter(is_active=False)
        serializer=CustomUserserializers(users, many=True)
        for user_data in serializer.data:
            if 'password' in user_data:
                user_data.pop('password')
        return Response(serializer.data, status=status.HTTP_200_OK)