from django.urls import path
from app_reg_login.views import MyView
from . import views


urlpatterns = [
    path('', MyView.as_view(), name='home'),

    # user management
    path('register/', views.signup, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('update/', views.updateUser, name='update'),
    path('profile/<str:pk>', views.profile, name='profile'),

    # auction Listing & bidding

]