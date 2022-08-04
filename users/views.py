from django.db.models.query import Prefetch
from django.shortcuts import render

from products.models import Deals
from users.models import CustomUser


def index(request):
    sellers = CustomUser.objects.prefetch_related(
        Prefetch(
            'sale',
            queryset=Deals.objects.select_related(
                'seller',
                'buyer'
            ).prefetch_related(
                'flowers',
                'deal__flowers'
            )
        )
    ).filter(role='seller')

    return render(
        request, 'index.html', {'sellers': sellers}
    )
