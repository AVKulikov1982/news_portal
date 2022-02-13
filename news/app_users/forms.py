from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
	last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
	email = forms.CharField(max_length=30, required=False, help_text='email')
	phone = forms.IntegerField(required=False, help_text='Номер телефона')
	city = forms.CharField(max_length=30, required=False, help_text='Город')
	card_number = forms.IntegerField(required=False, help_text='Номер карты')
	date_of_birth = forms.DateTimeField(required=False, help_text='Дата рождения')

	# verification = forms.BooleanField(required=False, help_text='Верификация')
	# count_news = forms.CharField(max_length=30, required=False, help_text='Количество новостей')

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'phone',
				  'city', 'card_number', 'date_of_birth', 'password1', 'password2']
