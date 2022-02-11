from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class UserLoginView(LoginView):
	template_name = 'app_users/login.html'


class UserLogoutView(LogoutView):
	template_name = 'app_users/logout.html'


def logout(request):
	return render(request, 'app_users/logout.html')
