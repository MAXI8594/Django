from django.http import HttpResponse
import datetime
def saludo (request):
    return HttpResponse ("Hola mundoo")
    
def segundavista (request):
    return HttpResponse ("Segunda vista")

def DiadeHoy (request):

    dia = datetime.datetime().now()
    texto = 'Hoy es: {}'.format(dia)
    return HttpResponse(texto)