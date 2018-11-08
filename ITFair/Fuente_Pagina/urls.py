from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clase2', views.clase2, name='clase2'),
    path('clase/<int:id>', views.clase, name="clase")
]