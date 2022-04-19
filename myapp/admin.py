from django.contrib import admin

from myapp.models import Goods
from .models import Goods

# Register your models here.
admin.site.register(Goods)