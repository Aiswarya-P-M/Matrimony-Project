from django.urls import path
from .views import ( UsercreateView,UserLoginView,UserLogoutView, UserdetailsView,
                     UserDeactivateView, ResetPasswordView,UserListView, DeactivateUserbyAdminView,
                     ActiveUsersListView,InactiveUsersListView
                )

urlpatterns=[
    path('',UsercreateView.as_view(),name='user_creation'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='lgout'),
    path('byId/',UserdetailsView.as_view(),name='user_details'),
    path('deactivate/',UserDeactivateView.as_view(),name='deactivate'),
    path('reset/', ResetPasswordView.as_view(), name='reset_password'),
    

    #Admin

    path('listusers/',UserListView.as_view(),name='list_users'),
    path('deactivateuser/<int:user_id>',DeactivateUserbyAdminView.as_view(),name='deactivate_user'),
    path('activeusers/',ActiveUsersListView.as_view(),name='active_users'),
    path('inactiveusers/', InactiveUsersListView.as_view(), name='inactive_users')
    
   
    
    

]