from django.contrib import admin
from products.models.product import Category, Product, Use, Feature, Banner


class UseInline(admin.TabularInline):
    model = Use
    extra = 1


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [UseInline, FeatureInline]
    list_display = ('id', 'product_name', 'category')
    search_fields = ('product_name', 'description')
    list_filter = ('category',)


@admin.register(Use)
class UseAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'text']
    search_fields = ['text', 'product__product_name']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'text']
    search_fields = ['text', 'product__product_name']

admin.site.register(Banner)
