from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .pagination import StandardResultsSetPagination

from users.serializers import GetUserSerializer
from rest_framework import viewsets,filters 
from users.models import User
from pagos.models import Servicios,Payment_user, Expired_payments
from .serializers import ServiciosSerializer, PaymentuserSerializer, ExpiredPaymentsSerializer
from django.shortcuts import redirect

class GetUsersViewset(viewsets.ModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()


class ServiciosViewset(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer
    pagination_class = StandardResultsSetPagination


class PaymentusersViewset(viewsets.ModelViewSet):
    queryset = Payment_user.objects.all()
    serializer_class = PaymentuserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['ExpirationDate','PaymentDate']

class ExpiredPaymentsViewset(viewsets.ModelViewSet):
    queryset = Expired_payments.objects.all()
    serializer_class = ExpiredPaymentsSerializer
    pagination_class = StandardResultsSetPagination
