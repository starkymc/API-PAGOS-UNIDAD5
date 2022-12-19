from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import SignUpSerializer, GetUserSerializer
from rest_framework import viewsets
from users.models import User
from django.shortcuts import redirect

class GetUsers(viewsets.ModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()
