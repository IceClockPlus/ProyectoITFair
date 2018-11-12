from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clase2', views.clase2, name='clase2'),
    path('clase/<int:id>', views.clase, name="clase"),
    path('nueva_clase',views.nueva_clase,name="nueva_clase")
]