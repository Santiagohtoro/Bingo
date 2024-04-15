from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/<str:username>", views.room_route, name="room"),
    path('usernameReg/<str:room_name>/', views.register_username, name='usernameReg')
]

    #path('crear_sala/', views.crear_sala, name='crear_sala'),
    #path('ingresar_nombre_usuario/<int:sala_id>/', views.ingresar_nombre_usuario, name='ingresar_nombre_usuario'),
    #path('sala/<int:sala_id>/', views.sala, name='sala'),