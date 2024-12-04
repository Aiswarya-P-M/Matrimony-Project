from django.urls import path
from .views import (
 SubscriptionCreateView,SubscriptionListView,
  SubscriptionRetrieveView,SubscriptionUpdateView,
  SubscriptionDeleteView,SubscribeplanView, UserBysubscriptionView
)

urlpatterns = [
    path('',SubscriptionCreateView.as_view(),name='create-subscription'),
    path('list/',SubscriptionListView.as_view(),name='list-subscription'),
    path('list/<int:pk>',SubscriptionRetrieveView.as_view(),name='retrieve-subscription'),
    path('update/<int:pk>', SubscriptionUpdateView.as_view(), name='update-subscription'),
    path('delete/<int:pk>', SubscriptionDeleteView.as_view(), name='delete-subscription'),
    path('subscribe/<int:user_id>/',SubscribeplanView.as_view(), name='subscribe-plan'),
    path('userbysubscription/<int:subscription_id>',UserBysubscriptionView.as_view(),name='user_by_subscription')
]