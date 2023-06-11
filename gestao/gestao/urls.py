from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.views import serve

from rest_framework import routers

#from simplecep.views import SimpleCepViewSet

#router = SimpleCepViewSet.as_view({'get': 'retrieve'}'})

route = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(route.urls)),
    # path('cep/<str:cep>/', router),
    path('cadastro/', include('cadastro.urls')),
    path('campeonato/', include('campeonato.urls')),
    path('evento/', include('evento.urls')),
    path('modalidade/', include('modalidade.urls')),
    #path('modalidades/', include('modalidade.urls')),  # Add this line
    
    
]

