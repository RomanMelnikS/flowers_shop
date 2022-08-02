from django.contrib import admin

from products.models import Flowers, Deals, DealDetails


class DealFlowerssAdmin(admin.TabularInline):
    list_display = (
        'flowers',
        'amount'
    )
    model = DealDetails


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


@admin.register(Deals)
class DealsAdmin(admin.ModelAdmin):

    def total_price(self, obj):
        details = DealDetails.objects.filter(deal=obj).values_list(
            'amount',
            flat=True
        )
        total_price = 0
        for flower in obj.flowers.all():
            for amount in details:
                total_price += amount * flower.price
        return total_price

    total_price.short_description = 'Итоговая цена'

    list_display = (
        'pk',
        'buyer',
        'total_price'
    )
    inlines = [
        DealFlowerssAdmin,
    ]


@admin.register(DealDetails)
class DealFlowersAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'deal',
        'flowers',
        'amount'
    )
