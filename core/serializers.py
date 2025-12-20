# from rest_framework import serializers
# from .models import Product


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
#         read_only_fields = ('created_at', 'updated_at')   

from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    # Kategoriyanıń tolıq ob'ektin kórsetiw ushın
    category = CategorySerializer(read_only=True)
    
    # Produkt qosqanda kategoriya ID-sin jiberiw ushın mınanı qosıń
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        source='category', 
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 
            'category', 'category_id', 'created_at', 'updated_at'
        ]
        read_only_fields = ('created_at', 'updated_at')



