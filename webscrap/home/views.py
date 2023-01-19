from django.shortcuts import render
from .helpers import *
from django.http import JsonResponse


def get_stock(request):
    get_all_stocks_urls()
    return JsonResponse({'status':200})
    
