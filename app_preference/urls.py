from django.urls import path
from .views import PreferenceCreateView,PreferencebyIdView

urlpatterns=[
    path('',PreferenceCreateView.as_view(),name='preference_creation'),
    path('preferencebyId/',PreferencebyIdView.as_view(),name='preferencebyId')
]