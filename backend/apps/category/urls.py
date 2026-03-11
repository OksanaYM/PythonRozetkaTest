from django.urls import path

from apps.category.views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView, \
    CategorySubCategoryCreateView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list'),
    path('/<int:pk>', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-delete'),
    path('/<int:pk>/subcategories', CategorySubCategoryCreateView.as_view(), name='category-sub-category-create'),


]