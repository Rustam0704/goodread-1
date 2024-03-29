from django.urls import path

from apps.users.views import UserLoginView, UserLogoutView, UserRegisterView, UserProfileView

app_name = "users"
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),

]
