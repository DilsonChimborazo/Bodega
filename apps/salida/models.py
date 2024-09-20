from django.db import models

# Create your models here.
class Salida(models.Model):
    categorias={
        ('metales','metales'),
        ('plasticos','Plasticos'),
    }
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(choices= categorias, max_length=50)
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre