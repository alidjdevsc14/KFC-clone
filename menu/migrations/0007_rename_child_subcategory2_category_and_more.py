# Generated by Django 4.1.6 on 2023-03-20 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_item_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory2',
            old_name='child',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='subcategory2',
            name='parent',
        ),
    ]
