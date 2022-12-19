from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', api.GetUsers, 'todosusers')

api_urlpatterns = router.urls