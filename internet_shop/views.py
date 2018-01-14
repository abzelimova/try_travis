from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from internet_shop.form import AddToBasketForm
from internet_shop.models import Category, Good, UserBasketItems
import uuid


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
    form = AddToBasketForm(good_id)
    good = get_object_or_404(Good, id=good_id)
    return render(request, 'internet_shop/good.html', {
        'title': good.name,
        'form': form,
        'categories': categories,
        'good_data' : good,
    })


def AddGood(request, item_id):
    if request.method == "POST":
        form = AddToBasketForm(item_id, data=request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            good = get_object_or_404(Good, id=item_id)

            if 'user_id' in request.COOKIES:
                uid = request.COOKIES.get('user_id')
            else:
                uid = uuid.uuid4()

            if (UserBasketItems.objects.filter(uid=uid, good=good, color=request.POST['color'], size=request.POST['size']).exists()):
                item = get_object_or_404(UserBasketItems, uid=uid, good=good, color=request.POST['color'], size=request.POST['size'])
                item.count_of += int(request.POST['count_of'])
                item.save()
            else:
                new_item.uid = uid
                new_item.good = good
                new_item.save()

        response = redirect(BasketView)
        response.set_cookie('user_id', uid)
        return response
    else:
        raise Http404()

def BasketView(request):
    categories = Category.objects.filter(parent__isnull=True)
    if 'user_id' not in request.COOKIES:
        user_id = uuid.uuid4()
    else:
        user_id = request.COOKIES.get('user_id')

    basket_items = UserBasketItems.objects.filter(uid=user_id)

    response = render(request, 'internet_shop/basket.html',{
        'title': "Корзина",
        'categories': categories,
        'basket_items': basket_items,
    })
    response.set_cookie('user_id', user_id)
    return response