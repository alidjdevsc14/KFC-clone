# Generated by Django 4.1.6 on 2023-03-20 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_subcategory_options_alter_subcategory2_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'It'},
        ),
    ]