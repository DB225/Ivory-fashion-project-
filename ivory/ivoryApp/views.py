from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'ivoryApp/index.html')


# MEN FUNCTIONS
def men(request):
    return render(request, 'ivoryApp/men.html')


def tshirtmen(request):
    return render(request, 'ivoryApp/tShirtMen.html')


def shirtmen(request):
    return render(request, 'ivoryApp/shirtMen.html')


def pantsmen(request):
    return render(request, 'ivoryApp/pantsMen.html')


def shoesmen(request):
    return render(request, 'ivoryApp/shoesMen.html')

#################################################################################
# WOMEN FUNCTIONS
def women(request):
    return render(request, 'ivoryApp/women.html')


def dress(request):
    return render(request, 'ivoryApp/dress.html')


def bagjewel(request):
    return render(request, 'ivoryApp/bagjewelry.html')


def shoeswomen(request):
    return render(request, 'ivoryApp/shoesWomen.html')
#################################################################################
def boys(request):
    return render(request, 'ivoryApp/boys.html')


def girls(request):
    return render(request, 'ivoryApp/girls.html')


def shoppingCart(request):
    return render(request, 'ivoryApp/shoppingCart.html')