from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.salida.models import Salida
from apps.salida.api.serializers import SalidaSerializers

class SalidaApiView(APIView):
    def get(self, request):
        serializer = SalidaSerializers(Salida.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self,request):
        serializer = SalidaSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)#validacion de datos correctos
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)