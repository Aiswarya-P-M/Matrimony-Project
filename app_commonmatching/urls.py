from django.urls import path
from .views import MatchingTableCreateView,MatchingTableListView,MasterTableCreateView, MasterTableListView

urlpatterns = [
    path('', MatchingTableCreateView.as_view(), name='matching-table-create'),
    path('getdetails/',MatchingTableListView.as_view(),name='matching-table-list'),
    path('master/', MasterTableCreateView.as_view(), name='master-table-create'),
    path('list/', MasterTableListView.as_view(),name='master-table-list')
]
