from django.shortcuts import render
from .models import Leccion, ItemLeccion

# Create your views here.
def index(request):
    return render(request,'index.html')

def clase2(request):
    return render(request,'clase2.html')

def clase(request, id):
    lec = Leccion.objects.get(pk = id)
    items = ItemLeccion.objects.filter(leccion = lec)
    return render(request,'clases.html',{'leccion':lec,'items':items})
