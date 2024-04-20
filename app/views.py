from django.shortcuts import render, redirect
from .models import Room, User
import random
from django.http import JsonResponse


def index(request):
    if request.method == 'POST':
        # Obtener el nombre de la sala del formulario
        room_name = request.POST.get('room_name')

        # Verificar si la sala ya existe en la base de datos
        existing_room = Room.objects.filter(room_name=room_name).exists()
        
        if existing_room:
            # Si la sala ya existe, redirigir a la página de registro de usuario
            return redirect(register_username, room_name=room_name)
        else:
            # Si la sala no existe, crear una nueva sala en la base de datos
            room = Room.objects.create(room_name=room_name)
            return redirect(register_username, room_name=room.room_name)
    return render(request, "index.html")

def register_username(request, room_name):
    if request.method == 'POST':
        username = request.POST['username']
        # Guardar el nombre de usuario en la base de datos
        room = Room.objects.get(room_name=room_name)
        if room.user_set.count() == 0:
            admin = True
            room.user_set.create(userName=username, admin=admin)
        else:
            room.user_set.create(userName=username)
            
        return redirect('room', room_name= room_name, username= username)
    return render(request, 'registeruser.html')

def room_route(request, room_name, username):
    print(request)
    user=User.objects.get(userName=username)
    userRole = "Administrador" if user.admin else "Jugador"
    imgn = random.randint(1,20)
    
    return render(request, "room.html", {"room_name": room_name, 'username': username, 'role': userRole, 'imgn': imgn})


# def distribuir_numero(request, room_id):
#     try:
#         # Obtener la sala especificada por room_id
#         sala = Room.objects.get(pk=room_id)
        
#         # Obtener todos los usuarios de la sala
#         usuarios = User.objects.filter(room=sala)
        
#         # Generar número aleatorio del 1 al 20
#         numero_aleatorio = random.randint(1, 20)
        
#         # Asignar el número aleatorio a todos los usuarios de la sala
#         for usuario in usuarios:
#             usuario.numero_aleatorio = numero_aleatorio
#             usuario.save()
        
#         return JsonResponse({'numero_aleatorio': numero_aleatorio})
    
#     except Room.DoesNotExist:
#         return JsonResponse({'error': 'La sala especificada no existe.'}, status=404)
