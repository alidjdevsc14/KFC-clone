from django.urls import path
from . import views

urlpatterns = [
    path('', views.userindex, name='home'),
    path('index/', views.index, name='admin'),
    path('category/', views.category, name='category'),
    path('category_list/<int:pk>/', views.category_list, name='category_list'),
    path('item_list/<int:pk>/', views.item_list, name='item_list'),
    path('item_list/', views.item_list, name='item_list'),
    path('order_list/', views.order_list, name='order_list'),
    path('sub_category_list/<int:pk>/', views.sub_category_list, name='sub_category_list'),
    path('subcategory/', views.subcategory, name='subcategory'),
    path('item/', views.item, name='item'),
    path('itemdetail/<int:item_id>/', views.item_detail, name='itemdetail'),
    path('order/', views.orders, name='order'),

]
