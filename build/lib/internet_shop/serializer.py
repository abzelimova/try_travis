from rest_framework import serializers

from internet_shop.models import Good

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        exclude = ()