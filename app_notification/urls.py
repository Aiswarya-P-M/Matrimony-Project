from django.urls import path
from .views import ( UnreadMessageNotificationView, NewMatchNotificationView, 
BulkMessageNotificationView, AddMasterTableEntryAndNotify, NotifyExpiringSubscriptionsView,
CreateSubscriptionPlanAndNotifyView, GetallNotificationView,GetallUnreadNotificationView
)

urlpatterns=[
   path('unread/<int:user_id>',UnreadMessageNotificationView.as_view(),name='unread_notification'),
   path('newmatch/',NewMatchNotificationView.as_view(), name='new_match_notification'),
   path('bulk/',BulkMessageNotificationView.as_view(),name='bulk_message'),
   path('addmaster/', AddMasterTableEntryAndNotify.as_view(), name='add_master_table_entry'),
   path('notifyexpiring/', NotifyExpiringSubscriptionsView.as_view(), name='notify_expiring_subscriptions'),
   path('notifysubscription/',CreateSubscriptionPlanAndNotifyView.as_view(),name='notify_subscription'),
   path('getall/',GetallNotificationView.as_view(), name='get_all_notification'),
   path('getallunread/',GetallUnreadNotificationView.as_view(), name='get_all_unread_notification')

]