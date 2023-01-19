from django.urls import path
from home.views import get_stock
urlpatterns = [
   path('get_stock/', get_stock, name='get_stock' ),
]
