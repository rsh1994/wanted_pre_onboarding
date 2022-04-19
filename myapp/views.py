from rest_framework import viewsets
from .serializers import GoodsSerializer
from .models import Goods

class GoodsViewset(viewsets.ViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    