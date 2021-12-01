from django.urls import path
from .views import CurrencyListAPIView, CategoryViewset, TransactionViewset
from rest_framework import routers

app_name = "core"

router = routers.SimpleRouter()
router.register(r"categories", CategoryViewset, basename="category")
router.register(r"transactions", TransactionViewset, basename="transaction")

urlpatterns = [
    # /currencies/
    path("currencies/", CurrencyListAPIView.as_view(), name="currencies"),
]

urlpatterns += router.urls
