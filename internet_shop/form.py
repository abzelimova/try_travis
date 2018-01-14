from internet_shop.models import UserBasketItems, Good
from django import forms

class AddToBasketForm(forms.ModelForm):
    def __init__(self, good, *args, **kwargs):
        super(AddToBasketForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['color'].queryset = Good.objects.filter(id=good).first().color
        self.fields['size'].queryset = Good.objects.filter(id=good).first().sizes

    class Meta:
        model = UserBasketItems
        exclude = ('good', )