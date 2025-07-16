from django.urls import path
from products.views.products import (
    CategoryWithProductsListAPIView,
    ProductDetailAPIView,
    BannerByCategoryView,
    CategoryWithFlatProductCardsView,
)

urlpatterns = [
    path('categories/', CategoryWithProductsListAPIView.as_view(), name='category-with-products'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('category/cards/', CategoryWithFlatProductCardsView.as_view(), name='category-cards-flat'),
    path('banner/', BannerByCategoryView.as_view(), name='category-banner'),
]
