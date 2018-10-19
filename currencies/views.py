from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View

from currencies.models import ExchangeRate


class ExchangeRatesView(View):
    def get(self, request):
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 20))

        exchanges_rates = ExchangeRate.objects.all().order_by('-updated')
        paginator = Paginator(exchanges_rates, page_size)

        return JsonResponse({
            "page": page,
            "page_size": page_size,
            "total": paginator.count,
            "data": list(paginator.page(page))
        })
