"""principal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Spectacular
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)


# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title= 'Pago API',
        default_version = 'v1',
        description = 'Proyecto Api de pagos',
        terms_of_service = 'https//www.google/policies/terms/',
        contact= openapi.Contact(email='contact@snippet.local'),
        license= openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagos.urls')),

    path('users/', include('users.urls')),


    #Rutas de Spectacular
    path('api/schema/',SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/',SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    # rutas deSwagger
    re_path(r'^swagger(?P<format>\.json|.yaml)$', schema_view.without_ui(cache_timeout=0),name="schema-json"),
    re_path(r'^swagger/$',schema_view.with_ui('swagger',cache_timeout=0), name="schema-swagger-ui"),
    re_path(r'^redoc/$',schema_view.with_ui('redoc',cache_timeout=0), name="schema-redoc"),

]