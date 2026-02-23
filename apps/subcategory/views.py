from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.product.models import ProductModel
from apps.product.serializers import ProductSerializer
from apps.subcategory.models import SubCategoryModel
from apps.subcategory.serializers import SubCategorySerializer



class SubCategoryRetrieveUpdateDestroyView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk_subcategory = kwargs['pk_subcategory']
        try:
            subcategory = SubCategoryModel.objects.get(pk=pk_subcategory)
        except SubCategoryModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, *args, **kwargs):
        pk_subcategory = kwargs['pk_subcategory']
        try:
            subcategory = SubCategoryModel.objects.get(pk=pk_subcategory)
        except SubCategoryModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = self.request.data
        serializer = SubCategorySerializer(subcategory, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, *args, **kwargs):
        pk_subcategory = kwargs['pk_subcategory']
        try:
            SubCategoryModel.objects.get(pk=pk_subcategory).delete()
        except SubCategoryModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)



class SubCategoryProductListCreateView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk_subcategory = kwargs['pk_subcategory']
        exist_subcategory = SubCategoryModel.objects.filter(pk=pk_subcategory)

        if not exist_subcategory:
            return Response(status=status.HTTP_404_NOT_FOUND)

        products = ProductModel.objects.filter(subcategory=pk_subcategory)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, *args, **kwargs):
        pk_subcategory = kwargs['pk_subcategory']
        exist_subcategory = SubCategoryModel.objects.filter(pk=pk_subcategory)

        if not exist_subcategory:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = self.request.data
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subcategory_id=pk_subcategory)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
