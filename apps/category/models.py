from django.db import models

from apps.core.enums.regex_enum import RegexEnum
from apps.core.models import BaseModel
from django.core import validators as V


class CategoryModel(BaseModel):
    class Meta:
        db_table = 'categories'

    name = models.CharField(max_length=255, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)] )





