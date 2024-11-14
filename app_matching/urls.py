from django.urls import path
from .views import FindMatchView 

urlpatterns = [
    # URL pattern for finding a match
    path('find-match/<int:user2_id>/', FindMatchView.as_view(), name='find_match'),
]
