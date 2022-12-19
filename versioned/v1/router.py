from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pago', api.TodosPagosViewset, 'todospagos')

api_urlpatterns = router.urls