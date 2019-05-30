from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'ivoryApp/index.html')


# New Designer
def newdesigner(request):
    newprofile = UserLoginForm(request.POST or None)
    print(request.POST)
    if request.method == 'POST' and newprofile.is_valid():
        UserLoginModel.objects.create(username=request.POST["username"], email=request.POST['email'],
                                      password=request.POST["password"], profilePic=request.POST["profilePic"])
        User.objects.create_user(request.POST["username"], request.POST['email'], request.POST["password"],
                                 request.POST["profilePic"])
        return redirect("index")
    return render(request, 'ivoryApp/newdesigner.html')


# MEN FUNCTIONS
def men(request):
    return render(request, 'ivoryApp/men.html')


# T-Shirt
def tshirtmen(request):
    allTshirts = Tshirt.objects.all()
    return render(request, 'ivoryApp/tShirtMen.html', {'allTshirts': allTshirts})


# new tShirt
def newtshirt(request):
    new_ts = TshirtForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_ts.is_valid():
        new_ts = TshirtForm(request.POST, request.FILES)

    return render(request, 'ivoryApp/newTshirt.html')


# read tShirt
def readtshirt(request):
    return render(request, 'ivoryApp/readTshirt.html')


# edit tShirt
def edittshirt(request):
    return render(request, 'ivoryApp/editTshirt.html')


# delete tShirt
def deletetshirt(request):
    return render(request, 'ivoryApp/deleteTshirt.html')

############################################


# Shirt
def shirtmen(request):
    return render(request, 'ivoryApp/shirtMen.html')


# new shirt
def newshirt(request):
    return render(request, 'ivoryApp/newShirt.html')


# read shirt
def readshirt(request):
    return render(request, 'ivoryApp/readShirt.html')


# edit shirt
def editshirt(request):
    return render(request, 'ivoryApp/editShirt.html')


# delete shirt
def deleteshirt(request):
    return render(request, 'ivoryApp/deleteShirt.html')

############################################


# Pants
def pantsmen(request):
    return render(request, 'ivoryApp/pantsMen.html')


# new pants
def newpants(request):
    return render(request, 'ivoryApp/newpants.html')


# read pants
def readpants(request):
    return render(request, 'ivoryApp/readpants.html')


# edit pants
def editpants(request):
    return render(request, 'ivoryApp/editpants.html')


# delete pants
def deletepants(request):
    return render(request, 'ivoryApp/deletepants.html')

############################################


# Shoes
def shoesmen(request):
    return render(request, 'ivoryApp/shoesMen.html')


# new men shoes
def newshoesmen(request):
    return render(request, 'ivoryApp/newshoesmen.html')


# read men shoes
def readshoesmen(request):
    return render(request, 'ivoryApp/readshoesmen.html')


# edit men shoes
def editshoesmen(request):
    return render(request, 'ivoryApp/editshoesmen.html')


# delete men shoes
def deleteshoesmen(request):
    return render(request, 'ivoryApp/deleteshoesmen.html')

####################################################################################
####################################################################################

# WOMEN FUNCTIONS


def women(request):
    return render(request, 'ivoryApp/women.html')


# Dress
def dress(request):
    return render(request, 'ivoryApp/dress.html')


# new dress
def newdress(request):
    return render(request, 'ivoryApp/newdress.html')


# read dress
def readdress(request):
    return render(request, 'ivoryApp/readdress.html')


# edit dress
def editdress(request):
    return render(request, 'ivoryApp/editdress.html')


# delete dress
def deletedress(request):
    return render(request, 'ivoryApp/deletedress.html')

############################################


# Bag & Jewelry
def bagjewel(request):
    return render(request, 'ivoryApp/bagjewel.html')


# new accessory
def newbagjewel(request):
    return render(request, 'ivoryApp/newbagjewel.html')


# read accessory
def readbagjewel(request):
    return render(request, 'ivoryApp/readbagjewel.html')


# edit accessory
def editbagjewel(request):
    return render(request, 'ivoryApp/editbagjewel.html')


# delete accessory
def deletebagjewel(request):
    return render(request, 'ivoryApp/deletebagjewel.html')

############################################


# Shoes
def shoeswomen(request):
    return render(request, 'ivoryApp/shoesWomen.html')


# new women shoes
def newshoeswomen(request):
    return render(request, 'ivoryApp/newshoeswomen.html')


# read women shoes
def readshoeswomen(request):
    return render(request, 'ivoryApp/readshoeswomen.html')


# edit women shoes
def editshoeswomen(request):
    return render(request, 'ivoryApp/editshoeswomen.html')


# delete women shoes
def deleteshoeswomen(request):
    return render(request, 'ivoryApp/deleteshoeswomen.html')
#################################################################################
#################################################################################


# Cart
def shoppingCart(request):
    return render(request, 'ivoryApp/shoppingCart.html')