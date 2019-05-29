from django import forms
from .models import Tshirt, Shirt, Pants, ShoesMen, ShoesWomen, Dress, BagJewel

CUSTOMER_SIZE = (
    ("s", "S"),
    ("m", "M"),
    ("l", "L"),
    ("xl", "XL"),
    ("xxl", "XXL"),
)

class TshirtForm(forms.ModelForm):
    models = Tshirt
    exclude = ["ts_ForeignKey"]
    labels = {
        'bj_title': 'Title',
        'bj_picture': 'Picture',
        'bj_size': 'Available Size',
        'bj_price': 'Price (USD)',
    }
    widgets = {
        'bj_size': forms.SelectMultiple()
    }