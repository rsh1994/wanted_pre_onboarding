from django.urls import path, include

from myapp.models import Goods
from .views import GoodsViewset
#GenericAPIView
#ArticleAPIView, ArticleDetails
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('goods', GoodsViewset, basename='goods')
urlpatterns = [
    # path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:id>/', ArticleDetails.as_view()),
    # path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
]
