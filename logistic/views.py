from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('products',)
    search_fields = ('products__title', 'products__description')
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # при необходимости добавьте параметры фильтрации
