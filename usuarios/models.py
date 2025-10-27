from django.db import models
from django.contrib.auth.models import User

# Definimos los roles disponibles
ROLES = (
    ('matrona', 'Matrona'),
    ('supervisor', 'Supervisor'),
)

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el usuario
    rol = models.CharField(max_length=20, choices=ROLES, default='matrona')  # Rol del usuario

    def __str__(self):
        return f"{self.user.username} - {self.rol}"