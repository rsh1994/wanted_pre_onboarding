from rest_framework import  serializers
from .models import Goods

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id','title', 'author','detail','one_amount','d_day','target_amount']
    
    def create(self, **validated_data):
        return Goods.objects.create(**validated_data)



"""
    title = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    detail = models.CharField(max_length=1000, blank=True)
    target_amount = models.IntegerField(null=False)
    one_amount = models.IntegerField(null=False)
    d_day = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.datetime.now)

    funding_rate = models.IntegerField(null=True)
    total_amount = models.IntegerField(null=True)
    n = models.IntegerField(default=0)
"""