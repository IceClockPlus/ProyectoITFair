from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('clase2', views.clase2, name='clase2'),
    path('clase/<slug:miurl>', views.clase, name="clase"),
    path('nueva_clase',views.nueva_clase,name="nueva_clase"),
    path('crear_clase',views.crear_clase,name="crear_clase"),
    path('nuevo_item',views.nuevo_item,name="nuevo_item"),
    path('crear_item',views.crear_item,name="crear_item"),
    path('lista_clases',views.lista_clases,name="lista_clases"),
    path('eliminar_clase/<int:id>',views.eliminar_clase,name="eliminar_clase"),
    path('lista_items/<int:id>',views.lista_items,name="lista_items")
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)