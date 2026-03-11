from rest_framework import serializers

from apps.product.models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = (
            'id',
            'name',
            'description',
            'stock',
            'price',
            'is_available',
            'views_count',
            'discount_price',
            'created_at',
            'updated_at',
        )

        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )


