
from django.contrib import admin
from django.urls import path
from Proyecto_1.views import saludo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segundavista/', saludo),
]
