from rest_framework.viewsets import ModelViewSet
from apps.registro.models import Registro
from apps.registro.api.serializers import registroSerializers

class SalidaModelViewSet(ModelViewSet):
    serializer_class= registroSerializers
    queryset = Registro.objects.all()