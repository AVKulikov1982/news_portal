# Generated by Django 2.2 on 2022-02-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='заголовок')),
                ('price', models.DecimalField(db_index=True, decimal_places=0, max_digits=5, verbose_name='цена')),
            ],
        ),
    ]
