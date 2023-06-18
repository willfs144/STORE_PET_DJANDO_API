from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r"^createorders$",views.OrderCreateAPIView.as_view(), name="createorders")
]