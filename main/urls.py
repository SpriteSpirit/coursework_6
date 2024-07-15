from django.urls import path

from main.apps import MainConfig
from main.views import index, contacts, noway_page

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('noway/', noway_page, name='noway'),
]
