# from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import  make_password

from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Preference
from .serializers import Preferenceserializers


class PreferenceCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        serializer=Preferenceserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Preference added successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        preference=Preference.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Or use PAGE_SIZE from settings.py
        paginated_preference = paginator.paginate_queryset(preference, request)
        serializer=Preferenceserializers(paginated_preference,many=True)
        return paginator.get_paginated_response(serializer.data)

class PreferencebyIdView(APIView):
    permission_classes= [permissions.IsAuthenticated]
    def get(self, request):
        try:
            # Use user_id instead of id
            preference = Preference.objects.get(user_id=request.user.user_id)
            serializer = Preferenceserializers(preference)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Preference.DoesNotExist:
            return Response({"message": "preference not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request):
        try:
            preference = Preference.objects.get(user_id=request.user.user_id)
            serializer = Preferenceserializers(preference, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Preference.DoesNotExist:
            return Response({"message": "Preference not found"}, status=status.HTTP_404_NOT_FOUND) 