from datetime import date
from django.db import models
from django.db.models import Manager, Model, F, Value, Q
from django.db.models.expressions import ExpressionWrapper
from django.db.models.fields import DecimalField


class PCSTradeManager(Manager):
    def get_queryset(self):
        return super(PCSTradeManager, self).get_queryset().annotate(
            income=ExpressionWrapper(F('count_contracts') * F('credit') * 100, output_field=DecimalField()),
            collateral=ExpressionWrapper((F('sell_strike') - F('buy_strike')) * F('count_contracts') * 100, output_field=DecimalField()),
            profit=ExpressionWrapper(0 if not F('closed_at') else F('income') - F('closed_at'), output_field=DecimalField()),
        )


class PCSTrade(Model):
    date_entry = models.DateField('EntryDate', blank=True, null=True)
    symbol = models.CharField('Symbol', max_length=10)
    date_expiration = models.DateField('ExpDate')
    buy_strike = models.DecimalField('Buy', decimal_places=2, max_digits=6)
    sell_strike = models.DecimalField('Sell', decimal_places=2, max_digits=6)
    credit = models.DecimalField('Credit', decimal_places=2, max_digits=6)
    count_contracts = models.PositiveIntegerField('Contracts')
    closed_at = models.DecimalField('ClosedAt', decimal_places=2, max_digits=6, blank=True, null=True)
    objects = PCSTradeManager()

    def __str__(self):
        return f'{self.date_entry} - {self.symbol} {self.count_contracts} - ${self.buy_strike}/${self.sell_strike} {self.date_expiration}'
    
    def display(self):
        return f'{self.count_contracts} contracts - ${self.buy_strike}/${self.sell_strike} {self.date_expiration}'

    def days_held(self):
        return 0 if self.date_entry is None else (self.date_expiration - self.date_entry).days

    def days_left(self):
        return (self.date_expiration - date.today()).days

    def return_on_investment(self):
        return self.income / self.collateral

    def return_on_investment_as_percent(self):
        return round(self.return_on_investment() * 100, 2)

    def annualized(self):
        if not self.closed_at or not self.days_held() or self.profit < 0:
            return 0
        return round(self.return_on_investment() / self.days_held(), 2)

    def annualized_as_percent(self):
        return round(self.annualized() * 10000, 0)
