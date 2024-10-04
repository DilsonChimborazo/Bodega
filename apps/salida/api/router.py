from rest_framework.routers import DefaultRouter
from apps.salida.api.views import SalidaModelViewSet

router_salida = DefaultRouter()
router_salida.register(prefix="salida", basename="salida", viewset=SalidaModelViewSet ) 