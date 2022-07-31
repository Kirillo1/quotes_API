from django.urls import path

from quotes_api.views import IndexView

app_name = 'quotes_api'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

