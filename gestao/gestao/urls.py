# gestao/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import (home_page)

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
   # path('cep/<str:cep>/', SimpleCepView.as_view(), name='cep-lookup'),  # Rota para a view SimpleCepView
    path('cadastro/', include('cadastro.urls')),
    path('campeonato/', include('campeonato.urls')),
    path('evento/', include('evento.urls')),
    path('modalidade/', include('modalidade.urls')),
]
