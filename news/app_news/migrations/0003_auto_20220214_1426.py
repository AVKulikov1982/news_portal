# Generated by Django 2.2 on 2022-02-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0002_auto_20220214_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='тэг'),
        ),
    ]