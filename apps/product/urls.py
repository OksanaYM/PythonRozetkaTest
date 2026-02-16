from django.urls import path

from apps.product.views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('/<int:pk_product>', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
]
