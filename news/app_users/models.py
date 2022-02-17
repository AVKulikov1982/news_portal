from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.IntegerField(verbose_name='Номер телефона')
	city = models.CharField(max_length=30, verbose_name='Город')
	card_number = models.IntegerField(verbose_name='Номер карты')
	date_of_birth = models.DateTimeField(db_index=True, verbose_name='Дата рождения')
	is_moderator = models.BooleanField(default=False, verbose_name='права модератора')
	is_verified = models.BooleanField(default=False, verbose_name='верификация')
	count_news = models.CharField(max_length=30, default=0, verbose_name='Количество новостей')

	class Meta:
		permissions = (('can_verified', 'может верифицировать'),)
