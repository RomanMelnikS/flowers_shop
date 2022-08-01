from django.db import models
from django.core.exceptions import ValidationError

from users.models import CustomUser


def seller_validation(value):
    seller = CustomUser.objects.get(id=value)
    if seller.role != 'seller':
        raise ValidationError(
            ('Покупатель не может создавать лоты товаров.'),
            params={'value': value},
        )


def buyer_validation(value):
    buyer = CustomUser.objects.get(id=value)
    if buyer.role != 'buyer':
        raise ValidationError(
            ('Продавец не может быть покупателем.'),
            params={'value': value},
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
    pass


class Feedback(models.Model):
    pass
