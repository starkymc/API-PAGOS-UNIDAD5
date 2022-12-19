from . import api
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users', api.GetUsersViewset, 'todosusers'),
router.register(r'servicios', api.ServiciosViewset, 'todosservicios'),
router.register(r'payment', api.PaymentusersViewset, 'todospayment'),
router.register(r'expired', api.ExpiredPaymentsViewset, 'expiredpayments'),

api_urlpatterns = router.urls