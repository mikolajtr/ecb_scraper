from django.urls import path

from currencies.views import CurrenciesView

urlpatterns = [
    path('', CurrenciesView.as_view()),
]