from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions,status

from .models import Subscription
from .serializers import SubscriptionSerializer

# 1. Create Subscription

class SubscriptionCreateView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAdminUser]

#2. List Subscription

class SubscriptionListView(generics.ListAPIView):
    queryset=Subscription.objects.all()
    serializer_class=SubscriptionSerializer
    permission_classes=[permissions.IsAdminUser]

#3. Retrieve Subscription

class SubscriptionRetrieveView(generics.RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAdminUser]

#4. Update Subscription

class SubscriptionUpdateView(generics.UpdateAPIView):
    queryset=Subscription.objects.all()
    serializer_class=SubscriptionSerializer
    permission_classes=[permissions.IsAdminUser]

#5. Delete Subscription

class SubscriptionDeleteView(generics.DestroyAPIView):
    queryset=Subscription.objects.all()
    serializer_class=SubscriptionSerializer
    permission_classes=[permissions.IsAdminUser]