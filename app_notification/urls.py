from django.urls import path
from .views import UnreadMessageNotificationView



urlpatterns=[
   path('unread/<int:user_id>',UnreadMessageNotificationView.as_view(),name='unread_notification')
]