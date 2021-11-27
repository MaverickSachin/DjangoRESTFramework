from typing import List
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Currency
from .serializers import CurrencySerializer


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
