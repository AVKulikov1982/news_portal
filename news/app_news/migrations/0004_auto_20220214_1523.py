# Generated by Django 2.2 on 2022-02-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_auto_20220214_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='создано'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='отредактировано'),
        ),
    ]
