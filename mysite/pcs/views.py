from django.shortcuts import render
from django.http import HttpResponse

from .models import PCSTrade

def index(request):
    records = PCSTrade.objects.order_by('-date_entry')
    output = ', '.join([q.symbol for q in records])
    return HttpResponse(output)

def detail(request, pcs_id):
    return HttpResponse(f'You are looking at {pcs_id}')
