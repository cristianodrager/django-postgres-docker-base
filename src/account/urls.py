from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_profile, name='account-profile'),
    path('signup/', views.account_signup, name='account-signup'),
    path('login/', views.account_login, name='account-login'),
    path('logout/', views.account_logout, name='account-logout'),
]
