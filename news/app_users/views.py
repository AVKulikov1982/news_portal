from django.shortcuts import render


class UserLoginView(LoginView):
	template_name = 'login.html'


class UserLogoutView(LogoutView):
	template_name = 'logout.html'


def logout(request):
	return render(request, 'logout.html')
