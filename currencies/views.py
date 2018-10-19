from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View

from currencies.models import ExchangeRate


class ExchangeRatesView(View):
    def get(self, request):
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 20))
        order_by = request.GET.get('order_by', '-updated')

        exchanges_rates = ExchangeRate.objects.all().order_by(order_by)
        paginator = Paginator(exchanges_rates, page_size)
        max_page = len(paginator.page_range)

        if page > max_page:
            page = max_page

        return JsonResponse({
            "page": page,
            "page_size": page_size,
            "total": paginator.count,
            "data": [{"currency": rate.currency,
                      "value": rate.value,
                      "updated": rate.updated} for rate in paginator.page(page)]
        })
