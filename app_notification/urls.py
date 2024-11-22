from django.urls import path
from .views import ( UnreadMessageNotificationView, NewMatchNotificationView, 
BulkMessageNotificationView, AddMasterTableEntryAndNotify
)

urlpatterns=[
   path('unread/<int:user_id>',UnreadMessageNotificationView.as_view(),name='unread_notification'),
   path('newmatch/',NewMatchNotificationView.as_view(), name='new_match_notification'),
   path('bulk/',BulkMessageNotificationView.as_view(),name='bulk_message'),
   path('addmaster/', AddMasterTableEntryAndNotify.as_view(), name='add_master_table_entry')
]