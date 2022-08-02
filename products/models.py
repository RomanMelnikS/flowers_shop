from django.db import models
from django.core.exceptions import ValidationError

from users.models import CustomUser


def seller_validation(value):
    seller = CustomUser.objects.get(id=value)
    if seller.role != 'seller':
        raise ValidationError(
            ('Покупатель не может создавать лоты товаров.'),
            params={'value': value}
        )


def buyer_validation(value):
    buyer = CustomUser.objects.get(id=value)
    if buyer.role != 'buyer':
        raise ValidationError(
            ('Продавец не может быть покупателем.'),
            params={'value': value}
        )


def visibility_validation(value):
    flower = Flowers.objects.get(id=value)
    if not flower.visibility:
        raise ValidationError(
            ('Продавец скрыл этот лот.'),
            params={'value': value}
        )


class Flowers(models.Model):

    COLOURS = [
        ('black', 'чёрный'),
        ('blue', 'голубой'),
        ('green', 'зелёный'),
        ('gray', 'серый'),
        ('olive', 'оливковый'),
        ('purple', 'пурпурный'),
        ('red', 'красный'),
        ('silver', 'серебристый'),
        ('white', 'белый'),
        ('yellow', 'жёлтый'),
        ('pink', 'розовый'),
        ('gold', 'золотой')
    ]

    seller = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        validators=[seller_validation],
        related_name='seller',
        verbose_name='Продавец',
        null=False
    )
    flower_type = models.CharField(
        max_length=100,
        verbose_name='Вид цветка',
        null=False
    )
    colour = models.CharField(
        max_length=50,
        verbose_name='Оттенок',
        choices=COLOURS,
        null=False
    )
    availability = models.PositiveIntegerField(
        verbose_name='Наличие',
        null=True
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена за шт.',
        null=False
    )
    visibility = models.BooleanField(
        verbose_name='Видимость',
        null=False
    )

    def __str__(self):
        return self.flower_type

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'


class Deals(models.Model):
    buyer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        validators=[buyer_validation],
        related_name='buyer',
        verbose_name='Покупатель',
        null=False
    )
    flowers = models.ManyToManyField(
        Flowers,
        through='DealDetails',
        related_name='flowers',
        verbose_name='Цветы',
        blank=True
    )

    def __str__(self):
        return self.buyer.username

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class DealDetails(models.Model):
    deal = models.ForeignKey(
        Deals,
        on_delete=models.CASCADE,
        related_name='deal',
        verbose_name='Заказ',
        null=False
    )
    flowers = models.ForeignKey(
        Flowers,
        on_delete=models.CASCADE,
        validators=[visibility_validation],
        related_name='deal_flowers',
        verbose_name='Цветы',
        null=False
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
        null=False
    )

    def clean(self):
        if self.amount > self.flowers.availability:
            raise ValidationError(
                ('Количество товара в заказе не может быть больше, \
                    чем в наличии.')
            )
        return super().clean()

    def save(self, *args, **kwargs):
        self.flowers.availability = self.flowers.availability - self.amount
        self.flowers.save()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.deal.buyer.username

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'


class Feedback(models.Model):
    pass
