from django.contrib import admin

from .models import *

class StockAdmin(admin.ModelAdmin):
    list_display= ['stock_name', 'stock_url']

admin.site.register(Stocks,StockAdmin)
