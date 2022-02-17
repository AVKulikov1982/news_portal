from django.db import models


class Items(models.Model):
	title = models.CharField(max_length=200, verbose_name='заголовок', db_index=True)
	price = models.DecimalField(max_digits=5, decimal_places=0, db_index=True, verbose_name='цена')
