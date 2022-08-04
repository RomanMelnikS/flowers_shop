from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ValidationError


class CustomUser(AbstractUser):

    class Role(models.TextChoices):
        BUYER = 'buyer', 'Покупатель'
        SELLER = 'seller', 'Продавец'

    role = models.CharField(
        choices=Role.choices,
        max_length=50,
        verbose_name='Роль пользователя',
        null=False
    )

    def check_deal_status(self, deal_id):
        if type(self).objects.filter(id=self.pk, buy=deal_id).exists():
            deal = self.buy.get(id=deal_id)
            return deal.status
        raise ValidationError(
            ('Такой сделки нет.'),
            code='users'
        )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
