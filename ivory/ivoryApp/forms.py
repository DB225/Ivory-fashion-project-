from django import forms
from .models import UserLoginModel, Tshirt, Shirt, Pants, ShoesMen, ShoesWomen, Dress, BagJewel

CUSTOMER_SIZE = (
    ("s", "S"),
    ("m", "M"),
    ("l", "L"),
    ("xl", "XL"),
    ("xxl", "XXL"),
)

CUSTOMER_SIZE_SHOES = (
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
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
            # 'ts_size': 'Available Size',
            'ts_price': 'Price (USD)',
        }
        # widgets = {
        #     'ts_size': forms.Select(choices=CUSTOMER_SIZE)
        # }


class ShirtForm(forms.ModelForm):
    class Meta:
        model = Shirt
        exclude = ["s_ForeignKey"]
        labels = {
            's_title': 'Title',
            's_picture': 'Picture',
            's_size': 'Available Size',
            's_price': 'Price (USD)',
        }
        # widgets = {
        #     's_size': forms.Select(choices=CUSTOMER_SIZE)
        # }


class PantsForm(forms.ModelForm):
    class Meta:
        model = Pants
        exclude = ["pant_ForeignKey"]
        labels = {
            'pant_title': 'Title',
            'pant_picture': 'Picture',
            'pant_size': 'Available Size',
            'pant_price': 'Price (USD)',
        }
        # widgets = {
        #     'pant_size': forms.Select(choices=CUSTOMER_SIZE)
        # }


class ShoesMenForm(forms.ModelForm):
    class Meta:
        model = ShoesMen
        exclude = ["sm_ForeignKey"]
        labels = {
            'sm_title': 'Title',
            'sm_picture': 'Picture',
            'sm_size': 'Available Size',
            'sm_price': 'Price (USD)',
        }
        # widgets = {
        #     'sm_size': forms.Select(choices=CUSTOMER_SIZE_SHOES)
        # }


class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        exclude = ["dress_ForeignKey"]
        labels = {
            'dress_title': 'Title',
            'dress_picture': 'Picture',
            'dress_size': 'Available Size',
            'dress_price': 'Price (USD)',
        }
        # widgets = {
        #     'dress_size': forms.Select(choices=CUSTOMER_SIZE)
        # }


class BagJewelForm(forms.ModelForm):
    class Meta:
        model = BagJewel
        exclude = ["bj_ForeignKey"]
        labels = {
            'bj_title': 'Title',
            'bj_picture': 'Picture',
            'bj_size': 'Available Size',
            'bj_price': 'Price (USD)',
        }
        # widgets = {
        #     'bj_size': forms.Select(choices=CUSTOMER_SIZE_ACCESSORY)
        # }


class ShoesWomenForm(forms.ModelForm):
    class Meta:
        model = ShoesWomen
        exclude = ["sw_ForeignKey"]
        labels = {
            'sw_title': 'Title',
            'sw_picture': 'Picture',
            'sw_size': 'Available Size',
            'sw_price': 'Price (USD)',
        }
        # widgets = {
        #     'sw_size': forms.Select(choices=CUSTOMER_SIZE_SHOES)
        # }


class MyForm(forms.Form):
    my_choice_field = forms.ChoiceField(choices=CUSTOMER_SIZE_ACCESSORY)
    ts_size = forms.ChoiceField(choices=CUSTOMER_SIZE)
    s_size = forms.ChoiceField(choices=CUSTOMER_SIZE)
    pant_size = forms.ChoiceField(choices=CUSTOMER_SIZE)
    sm_size = forms.ChoiceField(choices=CUSTOMER_SIZE_SHOES)
    dress_size = forms.ChoiceField(choices=CUSTOMER_SIZE)
    bj_size = forms.ChoiceField(choices=CUSTOMER_SIZE_ACCESSORY)
    sw_size = forms.ChoiceField(choices=CUSTOMER_SIZE_SHOES)