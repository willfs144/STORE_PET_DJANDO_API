from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r"^createorders$",views.OrderCreateAPIView.as_view(), name="createorders"),
    re_path(r"^getorders$",views.OrderListApi.as_view(), name="getorders"),
]