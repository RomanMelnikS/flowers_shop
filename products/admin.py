from django.contrib import admin

from products.models import Flowers, Deals


@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'seller',
        'flower_type',
        'colour',
        'availability',
        'price',
        'visibility'
    )
    model = Flowers


@admin.register(Deals)
class DealsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'buyer',
    )
    model = Deals
