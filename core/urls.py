from django.urls import path
from .views import CurrencyListAPIView, CategoryViewset
from rest_framework import routers

app_name = "core"

router = routers.SimpleRouter()
router.register(r"categories", CategoryViewset, basename="category")

urlpatterns = [
    # /currencies/
    path("currencies/", CurrencyListAPIView.as_view(), name="currencies"),
]

urlpatterns += router.urls
