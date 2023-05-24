from rest_framework.urls import path
from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet, HelloApiView

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
                  path('hello/', HelloApiView.as_view()),
              ] + router.urls
