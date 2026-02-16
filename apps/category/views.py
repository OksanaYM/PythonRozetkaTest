from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response

from apps.category.models import CategoryModel
from apps.category.serializers import CategorySerializer
from apps.subcategory.models import SubCategoryModel
from apps.subcategory.serializers import SubCategorySerializer


class CategoryListCreateView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ('get', 'put', 'delete' )


class CategorySubCategoryCreateView(GenericAPIView):

    def post(self, *args, **kwargs):
        pk_category = kwargs['pk']
        exist_category = CategoryModel.objects.filter(pk=pk_category).exists()

        if not exist_category:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = self.request.data
        serializer = SubCategorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(category_id=pk_category)

        return Response(serializer.data, status=status.HTTP_200_OK)

