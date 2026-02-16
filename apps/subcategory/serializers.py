from rest_framework import serializers

from apps.product.serializers import ProductSerializer
from apps.subcategory.models import SubCategoryModel


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = ('id', 'name', 'created_at', 'updated_at')