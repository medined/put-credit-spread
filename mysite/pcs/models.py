from django.db import models

class PCSTrade(models.Model):
    date_entry = models.DateField('EntryDate')
    symbol = models.CharField('Symbol', max_length=10)
    date_expiration = models.DateField('ExpDate')
    buy_strike = models.DecimalField('Buy', decimal_places=2, max_digits=6)
    sell_strike = models.DecimalField('Sell', decimal_places=2, max_digits=6)
    credit = models.DecimalField('Credit', decimal_places=2, max_digits=6)
    count_contracts = models.PositiveIntegerField('Contracts')
    closed_at = models.DecimalField('ClosedAt', decimal_places=2, max_digits=6, blank=True)
