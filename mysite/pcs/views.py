from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView

from .models import PCSTrade


class IndexView(generic.ListView):
    template_name = 'pcs/index.html'
    context_object_name = 'records'

# win_count = profit > 0
# loss_count = profit < 0

    def get_queryset(self):
        return PCSTrade.objects.order_by('-date_entry')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sum_income'] = round(sum(o.income for o in context['object_list']), 2)

        context['sum_collateral'] = 0
        for o in context['object_list']:
            if not o.closed_at:
                context['sum_collateral'] = context['sum_collateral'] + o.collateral

        context['sum_profit'] = round(sum(filter(None, (o.profit for o in context['object_list']))), 2)
        context['win_count'] = sum(o.profit is not None and o.profit > 0 for o in context['object_list'])
        context['loss_count'] = sum(o.profit is not None and o.profit < 0 for o in context['object_list'])
        return context


class DetailView(generic.DetailView):
    model = PCSTrade
    template_name = 'pcs/detail.html'


class AboutView(TemplateView):
    template_name = "about.html"


def detail(request, pk):
    record = get_object_or_404(PCSTrade, pk=pk)
    return render(request, 'pcs/detail.html', { 'record': record, })


def update(request, pk):
    record = get_object_or_404(PCSTrade, pk=pk)
    record.date_entry = request.POST['date_entry']
    record.symbol = request.POST['symbol']
    record.date_expiration = request.POST['date_expiration']
    record.buy_strike = request.POST['buy_strike']
    record.sell_strike = request.POST['sell_strike']
    record.credit = request.POST['credit']
    record.count_contracts = request.POST['count_contracts']
    record.closed_at = request.POST['closed_at']
    record.save()
    return HttpResponseRedirect(reverse('pcs:detail', args=(pk,)))
