# Generated by Django 4.1.6 on 2023-03-20 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_item_category_alter_item_sub_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'SubCategory'},
        ),
        migrations.AlterModelOptions(
            name='subcategory2',
            options={'verbose_name': 'SubCategory2', 'verbose_name_plural': 'SubCategory2'},
        ),
    ]
