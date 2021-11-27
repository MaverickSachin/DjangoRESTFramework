from django.urls import path
from .views import CurrencyListAPIView

app_name = "core"

urlpatterns = [
    # /currencies/
    path("currencies/", CurrencyListAPIView.as_view(), name="currencies"),
]
