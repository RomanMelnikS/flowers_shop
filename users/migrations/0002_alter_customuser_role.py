# Generated by Django 4.0.6 on 2022-08-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('buyer', 'Покупатель'), ('seller', 'Продавец')], max_length=50, verbose_name='Роль пользователя'),
        ),
    ]
