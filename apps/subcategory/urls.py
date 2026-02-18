from django.urls import path

from apps.subcategory.views import SubCategoryRetrieveUpdateDestroyView, SubCategoryProductListCreateView

urlpatterns = [
    path('/<int:pk_subcategory>', SubCategoryRetrieveUpdateDestroyView.as_view(), name='sub-category-retrieve-update-destroy'),
    path('/<int:pk_subcategory>/products', SubCategoryProductListCreateView.as_view(), name='sub-category-product-list-create'),
]