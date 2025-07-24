from products.models.product import Category, Product, Banner
from django.db.models import Prefetch


def get_all_categories_with_products(language=None):
    categories = Category.objects.all()
    if language:
        categories = categories.filter(language=language)
        return categories.prefetch_related(
            Prefetch(
                'products',
                queryset=Product.objects.filter(language=language)
            )
        )
    return categories.prefetch_related('products')


def get_product_by_id(product_id: int):
    return Product.objects.select_related('category').prefetch_related('features', 'uses').get(id=product_id)


def get_products_by_category(category_id: int):
    return Product.objects.filter(category_id=category_id)


def get_banner_by_category_id_and_language(category_id: int, language: str = 'Eng'):
    return Banner.objects.select_related('category').filter(
        category__id=category_id,
        language=language
    ).first()
