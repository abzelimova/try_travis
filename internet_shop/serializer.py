from rest_framework import serializers

from internet_shop.models import Good, UserBasketItems, User, Token, Order, Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        exclude = ()


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        exclude = ()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ()


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBasketItems
        exclude = ()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_staff',
            'last_login',
            'date_joined',
            'is_active',
            'groups',
            'user_permissions',
        )

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        exclude = ()