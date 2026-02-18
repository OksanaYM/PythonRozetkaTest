from django.urls import path

from apps.product.views import ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('/<int:pk_product>', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
]
