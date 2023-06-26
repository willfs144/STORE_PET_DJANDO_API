from django.urls import path
from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r"^createproducts$",views.ProductCreateAPI.as_view(), name="createproducts"),
    re_path(r"^getproducts$",views.ProductListAPI.as_view(), name="getproducts"),
    re_path(r'^updateproduct/(?P<pk>[0-9]+)$', views.ProductUpdateAPI.as_view(), name='updateproduct'),
    re_path(r'^detailproduct/(?P<pk>[0-9]+)$', views.ProductDetailAPI.as_view(), name='detailproduct'),
     re_path(r'^deleteproduct/(?P<pk>[0-9]+)$', views.ProductDeleteAPI.as_view(), name='deleteproduct'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product')  
]
