from rest_framework.routers import DefaultRouter
from apps.registro.api.views import SalidaModelViewSet

router_registro = DefaultRouter()
router_registro.register(prefix="registro", basename="registro", viewset=SalidaModelViewSet ) 