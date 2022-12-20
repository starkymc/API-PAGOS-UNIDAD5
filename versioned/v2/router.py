from . import api
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users', api.GetUsersViewset, 'todosusers'),
router.register(r'servicios', api.ServiciosViewset, 'todosservicios'),
router.register(r'payment', api.PaymentusersViewset, 'todospayment'),
router.register(r'expired', api.ExpiredPaymentsViewset, 'expiredpayments'),

    #path("signup/", views.SignUpView.as_view(), name="signup"),
    #path("login/", views.LoginView.as_view(), name="login"),
    #path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    #path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),

api_urlpatterns = router.urls