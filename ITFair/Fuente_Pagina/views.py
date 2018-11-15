from django.shortcuts import render
from django.http import HttpResponse
from .models import Leccion, ItemLeccion
from django.shortcuts import redirect
from .utils import conseguir_id_youtube
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout, login as auth_login


# Create your views here.
def index(request):
    lec = Leccion.objects.all()
    usuario = request.session.get('usuarioActual',None)
    return render(request,'index.html',{'lecciones':lec,'usuarioActual':usuario})

def clase2(request):
    return render(request,'clase2.html')

def clase(request, miurl):
    lec = Leccion.objects.get(url = miurl)
    items = ItemLeccion.objects.filter(leccion = lec)
    return render(request,'clases.html',{'leccion':lec,'items':items})

def nueva_clase(request):
    return render(request,'nuevaclase.html')

def crear_clase(request):
    nombre = request.POST.get('nombre')
    imgInp = request.FILES['imgInp']
    descripcion = request.POST.get('descripcion')
    video = request.POST.get('ylink','')
    youtube_id = conseguir_id_youtube(video)
    if youtube_id is not None:
        ylink = "http://www.youtube.com/embed/" + conseguir_id_youtube(video)
    else:
        return redirect('nueva_clase')

    lec = Leccion(titulo=nombre,resumen=descripcion,icono=imgInp,video=ylink)
    lec.save()
    return redirect('lista_clases')

def nuevo_item(request):
    lec = Leccion.objects.all()
    return render(request,'nuevoitem.html',{'lecciones':lec})

def crear_item(request):
    nombre = request.POST.get('nombre')
    imgInp = request.FILES['imgInp']
    descripcion = request.POST.get('descripcion')
    lec = Leccion.objects.filter(pk=request.POST.get('leccion'))[0]
    item = ItemLeccion(titulo=nombre,resumen=descripcion,icono=imgInp,leccion=lec)
    item.save()
    return redirect('lista_items',id=lec.pk)

def lista_clases(request):
    lec = Leccion.objects.all()
    return render(request,'listaclases.html',{'lecciones':lec})

def eliminar_clase(request, id):
    lec = Leccion.objects.filter(pk = id)[0]
    lec.delete()
    return redirect('index')

def lista_items(request, id):
    lec = Leccion.objects.filter(pk = id)[0]
    item = ItemLeccion.objects.filter(leccion = lec)
    return render(request,'listaitems.html',{'items':item,'leccion':lec})
    

def login(request):
    return render(request,'login.html')    

def iniciar_sesion(request):
    usuario = request.POST.get('usuario','')
    contrasenia = request.POST.get('contrasenia','')

    user = authenticate(request,username=usuario, password=contrasenia)
    if user is not None:
        auth_login(request,user)
        request.session['usuarioActual'] = user.first_name +" "+user.last_name
        return redirect('index')
    else:
        return redirect('login')        

def cerrar_sesion(request):
    del request.session['usuarioActual']
    logout(request)
    return redirect('index')