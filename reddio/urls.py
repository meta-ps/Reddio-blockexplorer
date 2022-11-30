from django.urls import path
from reddio.views import home,search_contract

urlpatterns = [
    path('', home, name='home'),
    path('contract/', search_contract, name='search_contract')
]
