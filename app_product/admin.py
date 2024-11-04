from django.contrib import admin
from django.contrib.auth.models import Group

from app_product.models import ProductModel
from app_user.models import UserModel


admin.site.register(ProductModel)
