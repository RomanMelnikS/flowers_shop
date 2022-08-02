# Generated by Django 4.0.6 on 2022-08-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DealFlowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Детали',
                'verbose_name_plural': 'Детали',
            },
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
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
                ('colour', models.CharField(choices=[('black', 'чёрный'), ('blue', 'голубой'), ('green', 'зелёный'), ('gray', 'серый'), ('olive', 'оливковый'), ('purple', 'пурпурный'), ('red', 'красный'), ('silver', 'серебристый'), ('white', 'белый'), ('yellow', 'жёлтый'), ('pink', 'розовый'), ('gold', 'золотой')], max_length=50, verbose_name='Оттенок')),
                ('availability', models.PositiveIntegerField(null=True, verbose_name='Наличие')),
                ('price', models.PositiveIntegerField(verbose_name='Цена за шт.')),
                ('visibility', models.BooleanField(verbose_name='Видимость')),
            ],
            options={
                'verbose_name': 'Цветок',
                'verbose_name_plural': 'Цветы',
            },
        ),
    ]
