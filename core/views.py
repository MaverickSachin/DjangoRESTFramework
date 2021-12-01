from typing import List
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Currency, Category, Transaction
from .serializers import CurrencySerializer, CategorySerializer, ReadTransactionSerializer, WriteTransactionSerializer


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class TransactionViewset(ModelViewSet):
    queryset = Transaction.objects.select_related("currency", "category")
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['amount', 'date']
    search_fields = ['description', ]
    filterset_fields = ['currency__code']

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ReadTransactionSerializer
        return WriteTransactionSerializer
