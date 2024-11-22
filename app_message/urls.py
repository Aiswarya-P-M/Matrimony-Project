from django.urls import path
from .views import (
    CreateMessageView,MessagebyReceiverView,UnreadMessageView, ViewMatchNotification, ViewBulkMessages
)
urlpatterns=[
    path('',CreateMessageView.as_view(),name='message_creation'),
    path('getnewmessages',MessagebyReceiverView.as_view(),name='getmessages'),
    path('unreadmessages/', UnreadMessageView.as_view(), name='unreadmessages'),
    path('viewmatch/',ViewMatchNotification.as_view(),name='viewmatch'),
    path('viewbulk/', ViewBulkMessages.as_view(), name='viewbulk')
    
   
]