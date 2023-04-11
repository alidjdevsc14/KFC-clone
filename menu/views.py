from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm, CategoryForm, SubCategoryForm, OrderForm
from .models import Category, SubCategory, Orders, Item
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.db.models import Sum


def index(request):
    if request.user.is_staff:
        return render(request, 'index.html')
    return redirect('home')


# def userindex(request):
#     return render(request, 'menu/userindex.html')


def userindex(request):
    if request.user.is_staff:
        return redirect('admin')
    category = Category.objects.all()
    orders = Orders.objects.values('item__name', 'item__image', 'item__price', 'item__description').annotate(
        total_orders=Sum('quantity')).order_by('-total_orders')[:4]
    print(orders.first())

    return render(request, 'menu/category_list.html', {'category': category, 'orders': orders})


def user_admin(request):
    category = Category.objects.all()
    return render(request, 'menu/category_list.html', {'category': category})


# def category(request):
#     form = CategoryForm()
#     if request.method == 'POST or FILES':
#         form = CategoryForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             form.save()
#
#     return render(request, "category.html", context={'form': form})


def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Do something with the saved form data
    else:
        form = CategoryForm()
    category = Category.objects.all()

    context = {
        'form': form,
        'category': category,

    }

    return render(request, 'category.html', context)


def subcategory(request):
    form = SubCategoryForm()
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, "subcategory.html", context={'form': form})


def all_item(request):
    item = Item.objects.all()
    return render(request, "item.html", context={'item': item})


# add item from staff user
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # category = obj.category.id

            return redirect('category')

    item = Item.objects.all()

    return render(request, "add_category.html", context={'form': form, 'item': item})


# add item from staff user
def item(request):
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            category = obj.category.id

            return redirect('items', category)

    item = Item.objects.all()

    return render(request, "add_item.html", context={'form': form, 'item': item})


# for user
def items(request, id):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    item = Item.objects.filter(category__id=id)

    return render(request, "item.html", context={'form': form, 'item': item})


def orders(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "order.html", context={'form': form})


def category_list(request, pk):
    category = Category.objects.filter(category__id=pk)

    return render(request, 'menu/category_list.html', {'category': category})


def sub_category_list(request, pk):
    sub_category = SubCategory.objects.filter(category__id=pk)
    return render(request, 'menu/sub_category_list.html', {'sub_category': sub_category})


def item_list(request, pk):
    item = Item.objects.filter(category__id=pk)
    return render(request, 'menu/item_list.html', {'item': item})


def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'menu/item_detail.html', {'item': item})


def order_list(request):
    all_order = Orders.objects.all()
    if request.method == 'POST':
        order_id = request.POST.get('item')
        order = get_object_or_404(Orders, id=order_id)
        order.delivered = True
        order.save()

    return render(request, 'order.html', {'order': all_order})


# cart views


# @login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def pre_order_add(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    return render(request, 'cart/cart1.html')


@login_required(login_url="/userlogin")
def checkout1(request, product__id=None):
    order = Orders.objects.filter(customer=request.user, delivered=False)

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        is_pickup = request.POST.get('is_pickup')
        user = request.user
        cart = request.session.get('cart')
        if cart:
            products = Item.objects.filter(id__in=(list(cart.keys())))
            if not order:

                for product in products:

                    order = Orders(item=product, customer=user, quantity=(cart.get(str(product.id))).get('quantity'),
                                   price=product.price,
                                   name=name,
                                   address=address,
                                   phone=phone,
                                   is_pickup=is_pickup)
                    total = order.item.quantity
                    ordered = order.quantity

                    # total = total + 1
                    if ordered > total:

                            # order.save()
                        if total != 0:
                            messages.error(request, f"Sorry..! {order.item} has only {total} items in stock.Bjt we have moved your order in Pre Order.")
                            order.save()
                            # return redirect('cart_detail')
                        if total == 0:
                            order.pre_order = True

                    order.save()
                    # print(order.quantity, 'order quantity---------------')
                    # print(order.item.quantity, 'order item quantity---------------')
                    # item = Item.objects.get(product__id=id)
                    if order.item.quantity > order.quantity:
                        order.item.quantity = order.item.quantity - order.quantity
                        order.item.sold = order.item.sold + order.quantity
                        order.item.save()
                    elif order.item.quantity < order.quantity:
                        order.item.pre_item = order.item.pre_item + order.quantity - order.item.quantity
                        order.item.sold = order.item.sold + order.quantity
                        order.item.quantity = 0
                        order.item.save()
                    # if order.item.quantity < order.quantity:


                request.session['cart'] = {}
            else:
                messages.error(request, 'You Have already order in pending!')
                # messages.success(request, 'You Have already order in pending!')
                return redirect('checkout')

        else:
            # messages.warning(request, 'No Product Found in Cart!')
            # messages.success(request, 'No Product Found in Cart!')
            messages.error(request, 'No Product Found in Cart!')
            return redirect('cart_detail')

    return redirect('checkout')


@login_required(login_url="/userlogin")
def checkout(request):
    order = Orders.objects.filter(customer=request.user)
    return render(request, 'checkout/checkout.html', {'order': order})


# Edit items
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item.save()
            messages.success(request, 'Item Updated!')

            # return render(request, 'item.html', {'form': form})
            return redirect('edit_item', item_id=item.id)
    return render(request, 'edit_item.html', {'form': form})


# Edit Category
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    return render(request, 'edit_category.html', {'form': form})


def top_selling_item(request):
    orders = Orders.objects.values('item__name', 'item__image', 'item__price', 'item__description').annotate(
        total_orders=Sum('quantity')).order_by('-total_orders')[:5]
    return render(request, 'top_selling_item.html', {'orders': orders})
