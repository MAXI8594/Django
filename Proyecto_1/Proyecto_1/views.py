from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo (request):
    return HttpResponse ("Hola mundoo")


def DiadeHoy (request):
    dia = datetime.datetime.now()
    texto = 'Hoy es: {}'.format(dia)
    return HttpResponse(texto)

def nombre_persona(self , nombre):
    resultado = "Mi nombre es : <br> <br> {}" .format(nombre)
    return HttpResponse(resultado)

#C:/Users/Usuario/Desktop/Django/Proyecto_1/Proyecto_1\plantilas\
def probandoTeamlates(self):

    nombre = 'Maxi'
    apellido = 'Olivera'
    dic = {"nombre":nombre,"apellido": apellido}

    miHtml = open( 'C:\\Users\\Usuario\\Desktop\\Django\\Proyecto_1\\Proyecto_1\\plantilas\\template1.html')
    plantilla = Template(miHtml.read())
    miHtml.close()

    miContexto = Context(dic)
    documento = plantilla.reader(miContexto)

    return HttpResponse(documento)