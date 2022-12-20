from pagos.models import Pagos
from rest_framework import viewsets
from .serializers import PagosSerializer
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle



class TodosPagosViewset(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['servicio']
    ordering = ('-id')

    # Defniendo Throttle
    #throttle_classes = [ UserRateThrottle,AnonRateThrottle]
    #throttle_classes = [ScopedRateThrottle]
    #throttle_scope = 'pagos'