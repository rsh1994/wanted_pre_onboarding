from rest_framework import viewsets
from .serializers import ServiceSerializer
from .models import Server
from rest_framework import permissions
from django_filters import rest_framework
from rest_framework import filters
ㅔ
class ServerViewSet(viewsets.ModelViewSet):
  queryset = Server.objects.all().order_by('-created_time')
  serializer_class = ServerSerializer
  pagination_class = MyFormatResultsSetPagination