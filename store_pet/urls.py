from django.contrib import admin

from django.urls import path
from django.urls import include

from . import views

from products.views import ProductListView

urlpatterns = [
    path('',ProductListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('productos/', include('products.urls')),
    path('categorias/', include('categories.urls')),
    path('ordenes/', include('orders.urls'))
]
