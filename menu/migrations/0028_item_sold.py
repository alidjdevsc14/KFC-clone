# Generated by Django 4.1.6 on 2023-04-11 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0027_remove_item_pre_order_remove_item_pre_order_limit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sold',
            field=models.IntegerField(default=0),
        ),
    ]
