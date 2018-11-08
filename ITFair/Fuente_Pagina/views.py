from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout, login as auth_login


# Create your views here.
def index(request):
    usuario = request.session.get('usuarioActual',None)
    return render(request,'index.html')

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