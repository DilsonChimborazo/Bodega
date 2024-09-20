from django.contrib import admin
from apps.registro.models import Registro
from apps.salida.models import Salida

# Register your models here.
admin.site.register(Registro)
admin.site.register(Salida)
