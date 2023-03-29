from django.contrib import admin
from .models import Category, SubCategory, Item, Orders

# Register your models here.


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)
admin.site.register(Orders)
