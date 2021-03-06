# Generated by Django 3.0.3 on 2021-07-31 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcstrade',
            name='closed_at',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='ClosedAt'),
        ),
        migrations.AlterField(
            model_name='pcstrade',
            name='date_entry',
            field=models.DateField(blank=True, null=True, verbose_name='EntryDate'),
        ),
    ]
