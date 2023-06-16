from django.urls import path
from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r"^getproducts$",views.ProductListApi.as_view(), name="getproducts"),
    path('<pk>', views.ProductDetailView.as_view(), name='product')  
]
