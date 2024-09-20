from rest_framework.serializers import ModelSerializer
from apps.registro.models import Registro

class registroSerializers(ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'