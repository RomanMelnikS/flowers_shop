# Generated by Django 4.0.6 on 2022-08-01 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_alter_flowers_options_flowers_visibility_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deals',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RenameField(
            model_name='flowers',
            old_name='amount',
            new_name='availability',
        ),
        migrations.AddField(
            model_name='deals',
            name='buyer',
            field=models.ForeignKey(default=bool, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL, validators=[products.models.buyer_validation], verbose_name='Покупатель'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deals',
            name='flowers',
            field=models.ManyToManyField(related_name='flowers', to='products.flowers', verbose_name='Цветы'),
        ),
        migrations.AlterField(
            model_name='flowers',
            name='visibility',
            field=models.BooleanField(verbose_name='Видимость'),
        ),
    ]