from rest_framework import  serializers
from .models import Server


class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Server
    fields = ('id', 'server_name', 'server_num', 'brand', 'model', 'cpus',
         'ram', 'disk', 'product_date', 'status', 'created_time',
         'modified_time')