from django.urls import path
from reddio.views import home,search_contract,user_data

urlpatterns = [
    path('', home, name='home'),
    path('contract/', search_contract, name='search_contract'),
    path('user/<str:pk>/', user_data,name='user')
]
