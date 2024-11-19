from django.urls import path
from .views import CreateMessageView,MessagebyReceiverView,UnreadMessageView

urlpatterns=[
    path('',CreateMessageView.as_view(),name='message_creation'),
    path('getmessages/',MessagebyReceiverView.as_view(),name='getmessages'),
    path('unreadmessages/', UnreadMessageView.as_view(), name='unreadmessages')
]