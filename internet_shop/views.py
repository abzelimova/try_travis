from django.shortcuts import render, get_object_or_404

from internet_shop.models import Category, Good


def IndexView(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'internet_shop/index.html',{
        'categories' : categories,
        'title' : 'My Shop',
    })

def CategoryView(request, category_name):
    categories = Category.objects.filter(parent__isnull=True)
    category = get_object_or_404(Category, url_name=category_name)
    goods = Good.objects.all().filter(category=category)
    return render(request, 'internet_shop/category.html', {
        'title': category.name,
        'categories' : categories,
        'goods' : goods,
    })

def GoodView(request, good_id):
    categories = Category.objects.filter(parent__isnull=True)
    good = get_object_or_404(Good, id=good_id)
    return render(request, 'internet_shop/good.html', {
        'title': good.name,
        'categories': categories,
        'good_data' : good,
    })