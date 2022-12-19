from . import api
from .api import * 
from rest_framework import routers
from django.urls import path, re_path, include

from versioned.v1.router import api_urlpatterns as api_v1
from versioned.v2.router import api_urlpatterns as api_v2

router = routers.DefaultRouter()

#router.register(r'pagos', api.PagoViewSet, 'pagos')

urlpatterns = [

    re_path(r'^api/v1/', include(api_v1)),
    re_path(r'^api/v2/', include(api_v2)),
]

urlpatterns += router.urls