from django.db import models

# Create your models here.


class Invitado(models.Model):
    numero = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30, null=True, blank=True)
    sexos = [
        ("H", 'Hombre'),
        ("M", 'Mujer'),
    ]
    sexo = models.CharField(
        max_length=2,
        choices=sexos,
        blank=True,
    )
    confirmado = models.BooleanField(default = False)
    cambio_nombre = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}".format(self.numero, self.nombre)

class Mensajes(models.Model):
    confirmacion = models.CharField(max_length=255)
    confirmacion_denegada = models.CharField(max_length=255)
    confirmacion_exitosa = models.CharField(max_length=255)
    comando_invalido = models.CharField(max_length=255)
    ya_confirmado = models.CharField(max_length=255)
    comandos_disponibles = models.CharField(max_length=255)
    mensaje_final = models.CharField(max_length=255)