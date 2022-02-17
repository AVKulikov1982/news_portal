from django.db import models
from django.contrib.auth.models import User


class News(models.Model):

	title = models.CharField(max_length=200, verbose_name='заголовок', db_index=True)
	content = models.CharField(max_length=500, verbose_name='содержание')
	created_at = models.DateField(auto_now_add=True, db_index=True, verbose_name='создано')
	updated_at = models.DateField(auto_now=True, verbose_name='отредактировано')
	flag = models.BooleanField(default=False, verbose_name='опубликовать')
	tag = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name='тэг')

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'news'
		ordering = ['created_at']
		permissions = (('can_published', 'может публиковать'), )


class Comment(models.Model):
	username = models.CharField(max_length=100, blank=True, null=True, verbose_name='имя пользователя')
	comment = models.CharField(max_length=200, verbose_name='комментарий')
	news = models.ForeignKey('News', null=False, related_name='comments',
								  on_delete=models.CASCADE, verbose_name='новость')
	user = models.ForeignKey(User, blank=True, null=True, related_name='comments',
							 	  on_delete=models.CASCADE, verbose_name='пользователь')

	def __str__(self):
		return f'{self.username} - {self.comment}'
