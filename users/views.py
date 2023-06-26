from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm
from .serializers import UserSerializer

#Librerias para la API
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView,
    ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, RetrieveDestroyAPIView, RetrieveAPIView)

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('index')

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username') #diccionario
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Usuario creado exitosamente")
            return redirect('index')
     
    return render(request, 'register.html',{
        'form': form
    })

#Seccion API
class UserListAPI(ListAPIView):  
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer    