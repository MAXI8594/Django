
from django.contrib import admin
from django.urls import path
from Proyecto_1.views import saludo
from Proyecto_1.views import DiadeHoy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segundavista/', saludo),
    path('diadehoy/', DiadeHoy),
]
