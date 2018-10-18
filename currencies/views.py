from django.http import JsonResponse
from django.views import View

from currencies.models import ExchangeRate


class ExchangeRatesView(View):
    def get(self, request):
        exchanges_rates = ExchangeRate.objects.all()
        return JsonResponse({
            "exchange_rates": list(exchanges_rates)
        })
