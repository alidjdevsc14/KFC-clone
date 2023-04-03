from django.urls import path
from . import views


urlpatterns = [
    path('', views.userindex, name='home'),
    path('index/', views.index, name='admin'),
    path('category/', views.category, name='category'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('category_list/<int:pk>/', views.category_list, name='category_list'),
    path('item_list/<int:pk>/', views.item_list, name='item_list'),
    path('item_list/', views.item_list, name='item_list'),
    path('order_list/', views.order_list, name='order_list'),
    path('sub_category_list/<int:pk>/', views.sub_category_list, name='sub_category_list'),
    path('subcategory/', views.subcategory, name='subcategory'),
    path('all_item/', views.all_item, name='all_item'),
    path('add_item/', views.item, name='item'),
    path('item/<int:id>/', views.items, name='items'),
    path('itemdetail/<int:item_id>/', views.item_detail, name='itemdetail'),
    path('order/', views.order_list, name='order'),

    # cart urls

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),


    # checkout

    path('check-out/', views.checkout, name='checkout'),
    path('checkout1/', views.checkout1, name='checkout1'),

    path('items/edit/<int:item_id>/', views.edit_item, name='edit_item'),
]
