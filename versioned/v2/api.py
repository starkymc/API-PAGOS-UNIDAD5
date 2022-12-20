from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle
from rest_framework import viewsets,filters 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from users.tokens import create_jwt_pair_for_user
from users.serializers import SignUpSerializer, GetUserSerializer
from users.models import User
from django.contrib.auth import authenticate

from .pagination import StandardResultsSetPagination
from pagos.models import Servicios,Payment_user, Expired_payments
from .serializers import ServiciosSerializer, PaymentuserSerializer, ExpiredPaymentsSerializer


class GetUsersViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserSerializer
    queryset = User.objects.all()


class ServiciosViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Servicios.objects.all()
    #serializer_class = ServiciosSerializer
    pagination_class = StandardResultsSetPagination
    def get_serializer_class(self):
        return ServiciosSerializer

    # listar
    def list(self, request):
       page = self.paginate_queryset(self.queryset)
       if page is not None:
          serializer = self.get_serializer(page, many=True)
          return self.get_paginated_response(serializer.data)
        
       serializer = self.get_serializer(self.queryset, many=True)
       return Response(serializer.data)

    #crear
    def create(self, request):
        if isinstance(request.data, list):
            serializer = ServiciosSerializer(data=request.data, many = True)
        else:
            serializer = ServiciosSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #por id
    def retrieve(self, request, pk=None):
        servicio = get_object_or_404(self.queryset, pk=pk)
        serializer = ServiciosSerializer(servicio)
        return Response(serializer.data)

    #actualizar
    def update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = ServiciosSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = ServiciosSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #Permisos de las vistas
    def get_permissions(self):
        if self.action == 'list' or self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class PaymentusersViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Payment_user.objects.all()
    serializer_class = PaymentuserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['ExpirationDate','PaymentDate']

    # Defniendo Throttle
    #throttle_classes = [ UserRateThrottle,AnonRateThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'pagos'

    


class ExpiredPaymentsViewset(viewsets.ViewSet):
    #queryset = Expired_payments.objects.all()
    #serializer_class = ExpiredPaymentsSerializer
    #pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Expired_payments.objects.all()
        serializer = ExpiredPaymentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Expired_payments.objects.all()
        serializer = ExpiredPaymentsSerializer(queryset, many=True)
        return Response(serializer.data)