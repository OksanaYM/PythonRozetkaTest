from django.db import models

from apps.category.models import CategoryModel
from apps.core.enums.regex_enum import RegexEnum
from apps.core.models import BaseModel

from django.core import validators as V


class SubCategoryModel(BaseModel):
    class Meta:
        db_table = 'subcategories'


    name = models.CharField(max_length=255, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)])
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='subcategories')
