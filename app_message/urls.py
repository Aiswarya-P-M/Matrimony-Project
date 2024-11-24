from django.urls import path
from .views import (
    CreateMessageView,MessagebyReceiverView, ViewMatchNotification,
    ViewBulkMessages, ViewMasterTableNotification, ViewRemindernotification
)
urlpatterns=[
    path('',CreateMessageView.as_view(),name='message_creation'),
    path('getnewmessages',MessagebyReceiverView.as_view(),name='getmessages'),
    # path('unreadmessages/', UnreadMessageView.as_view(), name='unreadmessages'),
    path('viewmatch/',ViewMatchNotification.as_view(),name='viewmatch'),
    path('viewbulk/', ViewBulkMessages.as_view(), name='viewbulk'),
    path('viewmaster/', ViewMasterTableNotification.as_view(), name='viewmaster'),
    path('viewreminder/', ViewRemindernotification.as_view(), name='viewreminder')
    
    
   
]