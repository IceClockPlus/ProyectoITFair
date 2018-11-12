from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('clase2', views.clase2, name='clase2'),
    path('clase/<int:id>', views.clase, name="clase"),
    path('nueva_clase',views.nueva_clase,name="nueva_clase"),
    path('crear_clase',views.crear_clase,name="crear_clase"),
    path('nuevo_item',views.nuevo_item,name="nuevo_item"),
    path('crear_item',views.crear_item,name="crear_item")
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)