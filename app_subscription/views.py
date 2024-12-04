from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions,status

from .models import Subscription
from .serializers import SubscriptionSerializer, CustomUserSubscriptionSerializer
from app_user.models import CustomUser



#Admin Operations

# 1. Create Subscription

class SubscriptionCreateView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAdminUser]

#2. List Subscription

class SubscriptionListView(generics.ListAPIView):
    queryset=Subscription.objects.all()
    serializer_class=SubscriptionSerializer
    permission_classes=[permissions.IsAuthenticated]

#3. Retrieve Subscription

class SubscriptionRetrieveView(generics.RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

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

# Users

#6. Subscribe to a plan

class SubscribeplanView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            # Get the user object
            user = CustomUser.objects.get(user_id=user_id)

            # Get the subscription plan selected by the user
            subscription_id = request.data.get('subscription_id')
            subscription = Subscription.objects.get(subscription_id=subscription_id)

            # Set the start date to the current date
            start_date = timezone.now()

            # Calculate the end date based on the subscription plan's duration
            end_date = subscription.calculate_end_date(start_date)

            # Update the user's subscription and subscription dates using .update()
            user.subscription_plan = subscription
            user.start_date = start_date
            user.end_date = end_date
            user.save()

            # Return the success message with start and end dates
            return Response({
                'message': f"You have successfully subscribed to the {subscription.plan_type} plan.",
                'start_date': start_date,
                'end_date': end_date
            }, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Subscription.DoesNotExist:
            return Response({'error': 'Subscription plan not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#7. Get the details of users under same subscription

class UserBysubscriptionView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, subscription_id):
        try:
            # Get the users filtered by subscription
            users = CustomUser.objects.filter(subscription_plan=subscription_id)

            # Initialize the paginator (using default pagination)
            paginator = PageNumberPagination()
            paginator.page_size = 10  # Define the default page size
            paginated_users = paginator.paginate_queryset(users, request)

            # Serialize the paginated users
            serializer = CustomUserSubscriptionSerializer(paginated_users, many=True)

            # Return paginated response
            return paginator.get_paginated_response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
