from django.urls import path

from app_users.views import UserLoginView, UserLogoutView, logout, register, account

urlpatterns = [
	path('user/login', UserLoginView.as_view(), name='login'),
	path('user/logout', UserLogoutView.as_view(), name='logout'),
	#path('logout/', logout, name='logout'),
	path('user/registration', register,  name='registration'),
	path('user/account', account,  name='account'),
]
