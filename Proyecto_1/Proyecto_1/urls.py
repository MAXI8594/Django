
from django.contrib import admin
from django.urls import path
from Proyecto_1.views import saludo
from Proyecto_1.views import DiadeHoy
from Proyecto_1.views import nombre_persona
from Proyecto_1.views import probandoTeamlates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),    
    path('diadehoy/', DiadeHoy),
    path('nombre_persona/<nombre>/', nombre_persona),
    path('probandoTeamlates/', probandoTeamlates)
]
