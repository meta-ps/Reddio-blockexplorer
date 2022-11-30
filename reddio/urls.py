from django.urls import path
from reddio.views import home

urlpatterns = [
    path('', home, name='home')
]
