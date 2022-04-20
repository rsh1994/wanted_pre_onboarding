from rest_framework import viewsets
from .serializers import GoodsSerializer
from .models import Goods

from rest_framework import status
from rest_framework.response import Response


from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

class GoodsViewset(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


goods_list = GoodsViewset.as_view({
    'get': 'list',
    'post': 'create',
})

goods_detail = GoodsViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
    # def create(self, request):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def list(self, request):
    #     goods = Goods.objects.all()
    #     serializer = GoodsSerializer(goods, many=True)
    #     return Response(serializer.data)

