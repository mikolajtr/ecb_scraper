from django.urls import path

from currencies.views import ExchangeRatesView

urlpatterns = [
    path('', ExchangeRatesView.as_view()),
]