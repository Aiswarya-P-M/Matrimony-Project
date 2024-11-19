from django.urls import path
from .views import FindMatchView, FindAllMatchesView

urlpatterns = [
    # URL pattern for finding a match
    path('find-match/', FindMatchView.as_view(), name='find_match'),
    path('find-all-matches/', FindAllMatchesView.as_view(), name='find_all_matches')
    
]
