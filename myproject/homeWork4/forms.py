import datetime

from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.Textarea()
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField(max_value=10000)
    image = forms.ImageField()
