"""django_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from internet_shop.views import IndexView, CategoryView, GoodView, BasketView, AddGood,GoodAPIView

router = routers.DefaultRouter()
router.register(r'goodAPI', GoodAPIView, base_name='goodAPI')

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # OUR:
    url(r'^$', IndexView, name='home'),
    url(r'catalog/(?P<category_name>\w+)/$', CategoryView, name="category"),
    url(r'basket/$', BasketView, name="basket_view"),
    url(r'addtobasket/(?P<item_id>\d+)/$', AddGood, name="basket_add"),
    url(r'good/(?P<good_id>\w+)/$', GoodView, name="good"),

    #API
    url(r'^api/v1/', include(router.urls)),
]

if settings.DEBUG == True:
    urlpatterns +=static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns +=static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
