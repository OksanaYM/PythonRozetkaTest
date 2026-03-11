from django.db import models

from apps.core.models import BaseModel
from apps.subcategory.models import SubCategoryModel


class ProductModel(BaseModel):
    class Meta:
        db_table = 'products'

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    subcategory =models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveIntegerField(default=1, blank=True)
    views_count = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    # def views_count_increment(self):
    #     ProductModel.objects.filter(pk=self.pk).update(views_count=models.F('views_count') + 1)

