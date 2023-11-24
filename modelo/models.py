from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    usuario_id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length = 70, null = False)
    apellidos = models.CharField(max_length = 70, null = False)
    correo = models.EmailField(max_length = 105, null = False, unique = True)
    date_created = models.DateTimeField(auto_now_add = True)
    autorizado = models.BooleanField(default = False)
    estado = models.BooleanField(default = True) # en el caso de que un alumno se retire, su estado pasara a false hasta decidir si se eliminara o no 

    def __str__(self):   
        return self.username
