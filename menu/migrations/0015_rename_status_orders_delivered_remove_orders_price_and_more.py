# Generated by Django 4.1.6 on 2023-03-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_alter_orders_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='status',
            new_name='delivered',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
