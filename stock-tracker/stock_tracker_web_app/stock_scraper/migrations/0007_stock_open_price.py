# Generated by Django 5.0.7 on 2024-08-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_scraper', '0006_delete_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='open_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
