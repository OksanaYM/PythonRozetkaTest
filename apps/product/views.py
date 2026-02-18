
# from apps.subcategory.models import SubCategoryModel
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.product.models import ProductModel
from apps.product.serializers import ProductSerializer


class ProductRetrieveUpdateDestroyView(GenericAPIView):
    def get(self, *args, **kwargs):
        pk_product = kwargs['pk_product']
        try:
            product = ProductModel.objects.get(pk=pk_product)
        except ProductModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk_product = kwargs['pk_product']
        try:
            product = ProductModel.objects.get(pk=pk_product)
        except ProductModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = self.request.data
        serializer = ProductSerializer(product, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk_product = kwargs['pk_product']
        try:
            ProductModel.objects.get(pk=pk_product).delete()
        except ProductModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)




#
# class ProductListCreateView(GenericAPIView):
#     def get(self, *args, **kwargs):
#         pk_category = kwargs['pk']
#         pk_subcategory = kwargs['pk_subcategory']
#         products = ProductModel.objects.filter(subcategory__category=pk_category, subcategory=pk_subcategory)
#         serializer = ProductSerializer(products, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         pk_category = kwargs['pk']
#         pk_subcategory = kwargs['pk_subcategory']
#         exist_subcategory = SubCategoryModel.objects.filter(category=pk_category, pk=pk_subcategory).exists()
#
#         if not exist_subcategory:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         data = self.request.data
#         serializer = ProductSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(subcategory_id=pk_subcategory)
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#
#
# class ProductRetrieveUpdateDestroyView(GenericAPIView):
#     def get(self, *args, **kwargs):
#         pk_category = kwargs['pk']
#         pk_subcategory = kwargs['pk_subcategory']
#         pk_product = kwargs['pk_product']
#         exist_subcategory = SubCategoryModel.objects.filter(category=pk_category, pk=pk_subcategory).exists()
#
#         if not exist_subcategory:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         try:
#             product = ProductModel.objects.get(
#                 subcategory__category=pk_category,
#                 subcategory=pk_subcategory,
#                 pk=pk_product,
#             )
#
#             # ProductModel.objects.filter(pk=self.pk).update(views_count=.F('views_count') + 1)
#             # product.views_count += 1
#         except ProductModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = ProductSerializer(product)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk_category = kwargs['pk']
#         pk_subcategory = kwargs['pk_subcategory']
#         pk_product = kwargs['pk_product']
#         exist_subcategory = SubCategoryModel.objects.filter(category=pk_category, pk=pk_subcategory).exists()
#
#         if not exist_subcategory:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         try:
#             product = ProductModel.objects.get(
#                 subcategory__category=pk_category,
#                 subcategory=pk_subcategory,
#                 pk=pk_product,
#             )
#         except ProductModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         data = self.request.data
#         serializer = ProductSerializer(product, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk_category = kwargs['pk']
#         pk_subcategory = kwargs['pk_subcategory']
#         pk_product = kwargs['pk_product']
#         exist_subcategory = SubCategoryModel.objects.filter(category=pk_category, subcategory=pk_subcategory).exists()
#         if not exist_subcategory:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         try:
#             ProductModel.objects.filter(subcategory__category=pk_category, subcategory=pk_subcategory,
#                                         pk=pk_product).delete()
#         except ProductModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         return Response(status=status.HTTP_204_NO_CONTENT)
