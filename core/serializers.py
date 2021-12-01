from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Category, Currency, Transaction


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "code", "name")


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ReadTransactionSerializer(ModelSerializer):
    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "currency",
            "date",
            "description",
            "category"
        )


class WriteTransactionSerializer(ModelSerializer):
    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())

    class Meta:
        model = Transaction
        fields = (
            "amount",
            "currency",
            "date",
            "description",
            "category"
        )
