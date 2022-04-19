from rest_framework import  serializers
from .models import Goods

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ('id','title', 'author','detail','one_amount','d_day')

