from django.shortcuts import render
from django.http import HttpResponse

def first_page(request):
    return render(request, 'first_page/base.html', {})
