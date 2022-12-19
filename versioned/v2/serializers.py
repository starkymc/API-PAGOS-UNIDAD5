from rest_framework import serializers
from pagos.models import Servicios


class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'
        read_only_fields = '__all__',