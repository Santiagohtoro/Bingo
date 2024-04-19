from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/<str:username>", views.room_route, name="room"),
    path('usernameReg/<str:room_name>/', views.register_username, name='usernameReg'),
    # path('repartir-numero/',views.distribuir_numero, name='distribuir_numero'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    #path('crear_sala/', views.crear_sala, name='crear_sala'),
    #path('ingresar_nombre_usuario/<int:sala_id>/', views.ingresar_nombre_usuario, name='ingresar_nombre_usuario'),
    #path('sala/<int:sala_id>/', views.sala, name='sala'),