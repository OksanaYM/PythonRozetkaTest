from django.urls import path, include

from apps.subcategory.views import SubCategoryRetrieveUpdateDestroyView

urlpatterns = [
    path('/<int:pk_subcategory>', SubCategoryRetrieveUpdateDestroyView.as_view(), name='sub-category-retrieve-update-destroy'),
    path('/<int:pk_subcategory>/products', include('apps.product.urls')),
]