from django.urls import path
from .views import CreateProfileView,ProfileDetailsView

urlpatterns=[
    path('',CreateProfileView.as_view(),name='profile_creation'),
    path('byid/',ProfileDetailsView.as_view(),name='profile_details')
   
    
    

]