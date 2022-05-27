from django.http import HttpResponse

def saludo (request):
    return HttpResponse ("Hola mundoo")
    
def segundavista (request):
    return HttpResponse ("Segunda vista")