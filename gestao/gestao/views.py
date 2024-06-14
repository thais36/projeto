from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home_page(request):
    return render(request, "home_page.html")