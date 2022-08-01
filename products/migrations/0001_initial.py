# Generated by Django 4.0.6 on 2022-08-01 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Flowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flower_type', models.CharField(max_length=100, verbose_name='Вид цветка')),
                ('colour', models.CharField(choices=[('#00ffff', 'aqua'), ('#000000', 'black'), ('#0000ff', 'blue'), ('#ff00ff', 'fuchsia'), ('#008000', 'green'), ('#808080', 'gray'), ('#00ff00', 'lime'), ('#800000', 'maroon'), ('#000080', 'navy'), ('#808000', 'olive'), ('#800080', 'purple'), ('#ff0000', 'red'), ('#c0c0c0', 'silver'), ('#008080', 'teal'), ('#ffffff', 'white'), ('#ffff00', 'yellow'), ('#ff1493', 'deeppink'), ('#deb887', 'burlywood'), ('#b8860b', 'darkgoldenrod'), ('#4b0082', 'indigo')], max_length=50, verbose_name='Оттенок')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL, validators=[products.models.seller_validation], verbose_name='Продавец')),
            ],
        ),
    ]
