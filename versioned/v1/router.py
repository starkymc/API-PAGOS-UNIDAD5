from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pagos', api.TodosPagosViewset, 'todospagos')

api_urlpatterns = router.urls