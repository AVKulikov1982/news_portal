from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.IntegerField(verbose_name='Номер телефона')
	city = models.CharField(max_length=30, verbose_name='Город')
	card_number = models.IntegerField(verbose_name='Номер карты')
	date_of_birth = models.DateTimeField(db_index=True, verbose_name='Дата рождения')
# verification = forms.BooleanField(required=False, help_text='Верификация')
# count_news = forms.CharField(max_length=30, required=False, help_text='Количество новостей')
