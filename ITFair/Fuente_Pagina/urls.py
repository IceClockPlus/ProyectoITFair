from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login,name='login'),
    path('login/iniciar',views.iniciar_sesion,name='iniciar_sesion'),
    path('login/cerrar',views.cerrar_sesion, name='cerrar_sesion'),
]