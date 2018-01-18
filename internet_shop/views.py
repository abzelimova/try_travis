from rest_framework.permissions import IsAuthenticated

from internet_shop.models import Category, Good, UserBasketItems, Order, Shop
# API
from internet_shop.serializer import GoodSerializer, BasketSerializer, TokenSerializer, ShopSerializer
from rest_framework.viewsets import GenericViewSet, mixins


class ShopAPIView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

class GoodAPIView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = GoodSerializer
    queryset = Good.objects.all()


class OrderAPIView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = Order
    queryset = Order.objects.all()


class BasketAPIView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketSerializer
    queryset = UserBasketItems.objects.all()


class AuthToken(mixins.CreateModelMixin,
                GenericViewSet):
    serializer_class = TokenSerializer

    def create(self, request, *args, **kwargs):
        original = TokenSerializer(
            serializer_class=self.serializer_class,
            request=request,
        )
        return original.post(request, *args, *kwargs)

