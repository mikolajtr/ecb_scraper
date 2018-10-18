from django.http import JsonResponse
from django.views import View


class CurrenciesView(View):
    def get(self, request):
        return JsonResponse({"message": "Hello world!"})