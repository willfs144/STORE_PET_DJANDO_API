from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from . import views
from products.views import ProductListView

from dj_rest_auth.registration.views import RegisterView


urlpatterns = [    
    path('', views.index, name='index' ),
    #path('',ProductListView.as_view(), name='index'),   
    path('productos/', include('products.urls')),
    path('categorias/', include('categories.urls')),
    path('ordenes/', include('orders.urls')), 
    path('accounts/', include('allauth.urls')),   
    path('usuarios/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', RegisterView.as_view(), name='rest_register')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)