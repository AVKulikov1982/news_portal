from django.urls import path

from app_users.views import UserLoginView, UserLogoutView, logout

urlpatterns = [
	path('user/login', UserLoginView.as_view(), name='login'),
	path('user/logout', UserLogoutView.as_view(), name='logout'),
	path('logout/', logout, name='logout'),
]
