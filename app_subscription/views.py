from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, permissions
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionCreateView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAdminUser]

class SubscriptionListView(generics.ListAPIView):
    queryset=Subscription.objects.all()
    serializer_class=SubscriptionSerializer
    permission_classes=[permissions.IsAdminUser]

class SubscriptionRetrieveView(generics.RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAdminUser]

class SubscriptionUpdateView(generics.UpdateAPIView):
    queryset=Subscription.objects.all()
    serializer_class=SubscriptionSerializer
    permission_classes=[permissions.IsAdminUser]

class SubscriptionDeleteView(generics.DestroyAPIView):
    queryset=Subscription.objects.all()
    serializer_class=SubscriptionSerializer
    permission_classes=[permissions.IsAdminUser]