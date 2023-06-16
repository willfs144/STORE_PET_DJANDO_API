from django.urls import path
from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r"^getcategories$",views.CategoryListApi.as_view(), name="getcategories")
]
