from rest_framework.viewsets import ModelViewSet
from apps.salida.models import Salida
from apps.salida.api.serializers import SalidaSerializers

class SalidaModelViewSet(ModelViewSet):
    serializer_class= SalidaSerializers
    queryset = Salida.objects.all()
