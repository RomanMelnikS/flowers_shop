from django.contrib import admin

from products.models import DealDetails, Deals, Feedback, Flowers


class DealDetailsInlineAdmin(admin.TabularInline):
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
        total_price = 0
        for flower in obj.deal.all():
            total_price += flower.amount * flower.flowers.price
        return total_price

    total_price.short_description = 'Итоговая цена'

    fields = (
        'buyer',
        'seller'
    )

    list_display = (
        'pk',
        'buyer',
        'seller',
        'total_price',
        'status'
    )
    inlines = [
        DealDetailsInlineAdmin,
    ]


@admin.register(DealDetails)
class DealDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'deal',
        'flowers',
        'amount'
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'seller',
        'flowers',
        'text'
    )
