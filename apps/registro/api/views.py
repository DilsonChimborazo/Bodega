from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.registro.models import Registro
from apps.registro.api.serializers import registroSerializers

class registroApiView(APIView):
    def get(self, request):
        serializer = registroSerializers(Registro.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self,request):
        serializer = registroSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)#validacion de datos correctos
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)