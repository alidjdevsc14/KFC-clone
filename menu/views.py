from django.shortcuts import render, redirect
from .forms import ItemForm, CategoryForm, SubCategoryForm, OrderForm
from .models import Category, SubCategory, Orders, Item

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
    context = {
        'form': form,
    }
    return render(request, 'category.html', context)


def subcategory(request):
    form = SubCategoryForm()
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, "subcategory.html", context={'form': form})


def item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, "item.html", context={'form': form})


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
    print(pk)
    sub_category = SubCategory.objects.filter(category__id=pk)
    return render(request, 'menu/sub_category_list.html', {'sub_category': sub_category})


# def item_list(request):
#     item = Item.objects.all()
#     return render(request, 'menu/item_list.html', {'item': item})

#
def item_list(request, pk):
    item = Item.objects.filter(category__id=pk)
    return render(request, 'menu/item_list.html', {'item': item})

def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'menu/item_detail.html', {'item': item})


def order_list(request):
    order = Orders.objects.all()
    return render(request, 'menu/order_list.html', {'order': order})
