# Generated by Django 3.0.3 on 2021-07-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PCSTrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entry', models.DateField(verbose_name='EntryDate')),
                ('symbol', models.CharField(max_length=10, verbose_name='Symbol')),
                ('date_expiration', models.DateField(verbose_name='ExpDate')),
                ('buy_strike', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Buy')),
                ('sell_strike', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sell')),
                ('credit', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Credit')),
                ('count_contracts', models.PositiveIntegerField(verbose_name='Contracts')),
                ('closed_at', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='ClosedAt')),
            ],
        ),
    ]