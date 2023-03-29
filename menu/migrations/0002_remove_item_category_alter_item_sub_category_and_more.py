# Generated by Django 4.1.6 on 2023-03-20 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AlterField(
            model_name='item',
            name='sub_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='menu.subcategory'),
        ),
        migrations.CreateModel(
            name='SubCategory2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.subcategory')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='sub_category2',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='menu.subcategory2'),
        ),
    ]
