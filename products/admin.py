from django.contrib import admin
from products.models import Product, ProductCategory, Basket


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name',
              'description',
              ('price', 'quantity'),
              'image',
              'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name',
              'description')
    ordering = ('name',)
    readonly_fields = ('name', 'description')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
