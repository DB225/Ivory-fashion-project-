from django import forms
from .models import UserLoginModel, Tshirt, Shirt, Pants, ShoesMen, ShoesWomen, Dress, BagJewel

CUSTOMER_SIZE = (
    ("s", "S"),
    ("m", "M"),
    ("l", "L"),
    ("xl", "XL"),
    ("xxl", "XXL"),
)


class UserLoginForm(forms.ModelForm):
    models = UserLoginModel
    exclude = ['userForeignKey']
    labels = {
        'username': 'Username',
        'email': 'Email',
        'password': 'Password',
        'profilePic': 'Photo',
    }
    widgets = {
        "password": forms.PasswordInput()
    }


class TshirtForm(forms.ModelForm):
    models = Tshirt
    exclude = ["ts_ForeignKey"]
    labels = {
        'ts_title': 'Title',
        'ts_picture': 'Picture',
        'ts_size': 'Available Size',
        'ts_price': 'Price (USD)',
    }
    widgets = {
        'ts_size': forms.Select(choices=CUSTOMER_SIZE)
    }


class ShirtForm(forms.ModelForm):
    models = Shirt
    exclude = ["s_ForeignKey"]
    labels = {
        's_title': 'Title',
        's_picture': 'Picture',
        's_size': 'Available Size',
        's_price': 'Price (USD)',
    }
    widgets = {
        's_size': forms.Select(choices=CUSTOMER_SIZE)
    }


class PantsForm(forms.ModelForm):
    models = Pants
    exclude = ["pant_ForeignKey"]
    labels = {
        'pant_title': 'Title',
        'pant_picture': 'Picture',
        'pant_size': 'Available Size',
        'pant_price': 'Price (USD)',
    }
    widgets = {
        'pant_size': forms.Select(choices=CUSTOMER_SIZE)
    }


class ShoesMenForm(forms.ModelForm):
    models = ShoesMen
    exclude = ["sm_ForeignKey"]
    labels = {
        'sm_title': 'Title',
        'sm_picture': 'Picture',
        'sm_size': 'Available Size',
        'sm_price': 'Price (USD)',
    }
    widgets = {
        'sm_size': forms.Select(choices=CUSTOMER_SIZE)
    }


class DressForm(forms.ModelForm):
    models = Dress
    exclude = ["dress_ForeignKey"]
    labels = {
        'dress_title': 'Title',
        'dress_picture': 'Picture',
        'dress_size': 'Available Size',
        'dress_price': 'Price (USD)',
    }
    widgets = {
        'dress_size': forms.Select(choices=CUSTOMER_SIZE)
    }


class BagJewelForm(forms.ModelForm):
    models = BagJewel
    exclude = ["bj_ForeignKey"]
    labels = {
        'bj_title': 'Title',
        'bj_picture': 'Picture',
        'bj_size': 'Available Size',
        'bj_price': 'Price (USD)',
    }
    widgets = {
        'bj_size': forms.Select(choices=CUSTOMER_SIZE)
    }


class ShoesWomenForm(forms.ModelForm):
    models = ShoesWomen
    exclude = ["sw_ForeignKey"]
    labels = {
        'sw_title': 'Title',
        'sw_picture': 'Picture',
        'sw_size': 'Available Size',
        'sw_price': 'Price (USD)',
    }
    widgets = {
        'sw_size': forms.Select(choices=CUSTOMER_SIZE)
    }