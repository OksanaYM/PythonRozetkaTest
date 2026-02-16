from rest_framework import serializers

from apps.category.models import CategoryModel
from apps.subcategory.serializers import SubCategorySerializer


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'subcategories', 'created_at', 'updated_at')
