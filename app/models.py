from django.db import models

# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    # Otros campos de la sala, si es necesario
    
    def __str__(self):
        return self.room_name

class User(models.Model):
    userName= models.CharField(max_length=100)
    admin = models.BooleanField(default=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # Otros campos del usuario, si es necesario
    
    def __str__(self):
        return self.userName
