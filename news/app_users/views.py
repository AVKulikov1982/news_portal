from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile


class UserLoginView(LoginView):
	template_name = 'app_users/login.html'


class UserLogoutView(LogoutView):
	template_name = 'app_users/logout.html'


def register(request):
	if request.method == 'POST':
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			user = register_form.save()
			card_number = register_form.cleaned_data.get('card_number')
			date_of_birth = register_form.cleaned_data.get('date_of_birth')
			city = register_form.cleaned_data.get('city')
			phone = register_form.cleaned_data.get('phone')
			Profile.objects.create(
				user=user,
				phone=phone,
				city=city,
				date_of_birth=date_of_birth,
				card_number=card_number
			)
			username = register_form.cleaned_data.get('username')
			row_password = register_form.cleaned_data.get('password1')

			user = authenticate(username=username, password=row_password)
			login(request, user)
			return redirect('/')
	else:
		register_form = RegisterForm()
	return render(request, 'app_users/registration.html', context={'register_form': register_form})


def account(request):

	return render(request, 'app_users/account.html')


def logout(request):
	return render(request, 'app_users/logout.html')
