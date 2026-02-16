from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps import subcategory
from apps.category.models import CategoryModel
from apps.subcategory.models import SubCategoryModel
from apps.subcategory.serializers import SubCategorySerializer



class SubCategoryRetrieveUpdateDestroyView(GenericAPIView):
    pass


    # queryset = SubCategoryModel.objects.all()
    # serializer_class = SubCategorySerializer
    # def get(self, *args, **kwargs):
    #     pk_category = kwargs['pk']
    #     pk_subcategory = kwargs['pk_subcategory']
    #     exist_category = CategoryModel.objects.filter(pk=pk_category).exists()
    #     if not exist_category:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     try:
    #         subcategory = SubCategoryModel.objects.get(category=pk_category, pk=pk_subcategory)
    #     except SubCategoryModel.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     serializer = SubCategorySerializer(subcategory)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # def put(self, *args, **kwargs):
    #     pk_category = kwargs['pk']
    #     pk_subcategory = kwargs['pk_subcategory']
    #     exist_category = CategoryModel.objects.filter(pk=pk_category).exists()
    #     if not exist_category:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     try:
    #         subcategory = SubCategoryModel.objects.get(category=pk_category, pk=pk_subcategory)
    #     except SubCategoryModel.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     data = self.request.data
    #     serializer = SubCategorySerializer(subcategory, data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # def delete(self, *args, **kwargs):
    #     pk_category = kwargs['pk']
    #     pk_subcategory = kwargs['pk_subcategory']
    #     exist_category = CategoryModel.objects.filter(pk=pk_category).exists()
    #     if not exist_category:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     try:
    #         SubCategoryModel.objects.filter(category=pk_category, pk=pk_subcategory).delete()
    #     except SubCategoryModel.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    #
