from django.urls import path
from .views import (
    CreateMessageView,MessagebyReceiverView, ViewMatchNotification,
    ViewBulkMessages, ViewMasterTableNotification, ViewRemindernotification,NewSubscriptionNotificationsView,
    SendRequestView, ViewRequest, UpdateRequestStatusView,UnreadMessageView,ViewMessageHistory
    
)
urlpatterns=[
    path('',CreateMessageView.as_view(),name='message_creation'),
    path('messagebyreceiver/',MessagebyReceiverView.as_view(),name='getmessages'),
    path('unreadmessages/', UnreadMessageView.as_view(), name='unreadmessages'),
    path('viewhistory/<int:other_user_id>/',ViewMessageHistory.as_view(), name='view_history'),
    path('viewmatch/',ViewMatchNotification.as_view(),name='viewmatch'),
    path('viewbulk/', ViewBulkMessages.as_view(), name='viewbulk'),
    path('viewmaster/', ViewMasterTableNotification.as_view(), name='viewmaster'),
    path('viewreminder/', ViewRemindernotification.as_view(), name='viewreminder'),
    path('newsubscription/', NewSubscriptionNotificationsView.as_view(), name='newsubscription'),
    
    #Request
    path('sendrequest/',SendRequestView.as_view(),name='sendrequest'),
    path('viewrequest/', ViewRequest.as_view(), name='viewrequest'),
    path('updaterequest/', UpdateRequestStatusView.as_view(), name='updaterequest'),

   
]