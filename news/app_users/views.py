from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthForm, RegisterForm, ModeratorForm, VerifiedForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from .models import Profile
from django.views import generic, View
from django.http import HttpResponseRedirect


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
		Group.objects.get_or_create(name='moderators')
		Group.objects.get_or_create(name='verified')
		register_form = RegisterForm()
	return render(request, 'app_users/registration.html', context={'register_form': register_form})


def account(request):
	return render(request, 'app_users/account.html')


# def logout(request):
# 	return render(request, 'app_users/logout.html')


class AppModeratorListView(generic.ListView):
	model = Profile
	template_name = 'app_users/moderators_list.html'
	context_object_name = 'users_list'
	queryset = Profile.objects.all()


class UpdateModeratorView(View):

	@staticmethod
	def get(request, user_id):
		profile = Profile.objects.get(id=user_id)
		username = profile.user.username
		user_form = ModeratorForm(instance=profile)
		return render(request, 'app_users/moderators_detail.html', context={'user_form': user_form, 'user_id': user_id,
																			'username': username})

	@staticmethod
	def post(request, user_id):
		profile = Profile.objects.get(id=user_id)
		user_form = ModeratorForm(request.POST, instance=profile)
		if user_form.is_valid():
			profile.save()
			group = Group.objects.get(name='moderators')
			group.user_set.add(profile.user)
		return HttpResponseRedirect('/')


class AppVerifiedListView(generic.ListView):
	model = Profile
	template_name = 'app_users/verified_list.html'
	context_object_name = 'users_list'
	queryset = Profile.objects.all()


class UpdateVerifiedView(View):
	@staticmethod
	def get(request, user_id):
		profile = Profile.objects.get(id=user_id)
		username = profile.user.username
		user_form = VerifiedForm(instance=profile)
		return render(request, 'app_users/verified_detail.html', context={'user_form': user_form, 'user_id': user_id,
																			'username': username})

	@staticmethod
	def post(request, user_id):
		profile = Profile.objects.get(id=user_id)
		user_form = VerifiedForm(request.POST, instance=profile)
		if user_form.is_valid():
			profile.save()
			group = Group.objects.get(name='verified')
			group.user_set.add(profile.user)
		return HttpResponseRedirect('/')
