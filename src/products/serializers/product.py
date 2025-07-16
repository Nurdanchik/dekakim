from rest_framework import serializers
from products.models.product import Product, Category, Feature, Use, Banner


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'logo', 'name', 'description']


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'text']


class UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Use
        fields = ['id', 'text']


class ProductSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)
    uses = UseSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'face_img',
            'slogan',
            'product_name',
            'description',
            'category',
            'features',
            'code',
            'subcode',
            'uses',
        ]


class ProductCardsFlatSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='category.id', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_logo = serializers.ImageField(source='category.logo', read_only=True)
    category_description = serializers.CharField(source='category.description', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'code',
            'subcode',
            'slogan',
            'description',
            'face_img',
            'category_id',
            'category_name',
            'category_logo',
            'category_description',
        ]


class CategoryWithFlatProductCardsSerializer(serializers.ModelSerializer):
    products = ProductCardsFlatSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products']


class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'code', 'subcode']


class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = ProductShortSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products']


class BannerSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Banner
        fields = ['id', 'category', 'slogan', 'description', 'photo']
