# Generated by Django 4.1.6 on 2023-04-02 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0018_orders_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
