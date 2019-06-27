from django import forms
from .models import UserLoginModel, Tshirt, Shirt, Pants, ShoesMen, ShoesWomen, Dress, BagJewel

CUSTOMER_SIZE = (
    ("s", "S"),
    ("m", "M"),
    ("l", "L"),
    ("xl", "XL"),
    ("xxl", "XXL"),
)

CUSTOMER_SIZE_SHOES_MEN = (
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
)

CUSTOMER_SIZE_SHOES_WOMEN = (
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
)


CUSTOMER_SIZE_ACCESSORY = (
    ("s", "S"),
    ("m", "M"),
)


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLoginModel
        exclude = ['userForeignKey']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
        }
        widgets = {
            "password": forms.PasswordInput()
        }


class TshirtForm(forms.ModelForm):
    class Meta:
        model = Tshirt
        exclude = ["ts_ForeignKey"]
        labels = {
            'ts_title': 'Title',
            'ts_picture': 'Picture',
            'ts_price': 'Price (USD)',
        }


class ShirtForm(forms.ModelForm):
    class Meta:
        model = Shirt
        exclude = ["s_ForeignKey"]
        labels = {
            's_title': 'Title',
            's_picture': 'Picture',
            's_price': 'Price (USD)',
        }


class PantsForm(forms.ModelForm):
    class Meta:
        model = Pants
        exclude = ["pant_ForeignKey"]
        labels = {
            'pant_title': 'Title',
            'pant_picture': 'Picture',
            'pant_price': 'Price (USD)',
        }


class ShoesMenForm(forms.ModelForm):
    class Meta:
        model = ShoesMen
        exclude = ["sm_ForeignKey"]
        labels = {
            'sm_title': 'Title',
            'sm_picture': 'Picture',
            'sm_price': 'Price (USD)',
        }


class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        exclude = ["dress_ForeignKey"]
        labels = {
            'dress_title': 'Title',
            'dress_picture': 'Picture',
            'dress_price': 'Price (USD)',
        }


class BagJewelForm(forms.ModelForm):
    class Meta:
        model = BagJewel
        exclude = ["bj_ForeignKey"]
        labels = {
            'bj_title': 'Title',
            'bj_picture': 'Picture',
            'bj_price': 'Price (USD)',
        }


class ShoesWomenForm(forms.ModelForm):
    class Meta:
        model = ShoesWomen
        exclude = ["sw_ForeignKey"]
        labels = {
            'sw_title': 'Title',
            'sw_picture': 'Picture',
            'sw_price': 'Price (USD)',
        }


class MyForm(forms.Form):
    ts_size = forms.ChoiceField(choices=CUSTOMER_SIZE)
    s_size = forms.ChoiceField(choices=CUSTOMER_SIZE)
    pant_size = forms.ChoiceField(choices=CUSTOMER_SIZE)
    sm_size = forms.ChoiceField(choices=CUSTOMER_SIZE_SHOES_MEN)
    dress_size = forms.ChoiceField(choices=CUSTOMER_SIZE)
    bj_size = forms.ChoiceField(choices=CUSTOMER_SIZE_ACCESSORY)
    sw_size = forms.ChoiceField(choices=CUSTOMER_SIZE_SHOES_WOMEN)