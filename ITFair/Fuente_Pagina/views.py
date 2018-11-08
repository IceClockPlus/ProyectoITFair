from django.shortcuts import render
from .models import Leccion

# Create your views here.
def index(request):
    return render(request,'index.html')

def clase2(request):
    return render(request,'clase2.html')

def clase(request, id):
    lec = Lecciones.objects.get(pk = id)
    return render(request,'clases.html',{lec})