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
                                      password=request.POST["password"])
        User.objects.create_user(request.POST["username"], request.POST['email'], request.POST["password"])
    return render(request, 'ivoryApp/newdesigner.html', {'newprofile': newprofile})


# MEN FUNCTIONS
def men(request):
    return render(request, 'ivoryApp/men.html')


# T-Shirt
def tshirtmen(request):
    allTshirts = Tshirt.objects.all()
    return render(request, 'ivoryApp/item/tShirtMen.html', {'allTshirts': allTshirts})


# new T-Shirt
def newtshirt(request):
    new_ts = TshirtForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_ts.is_valid():
        new_ts = TshirtForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        Tshirt.objects.create(ts_title=request.POST["ts_title"], ts_size=request.POST["ts_size"],
                              ts_picture=request.FILES["ts_picture"], ts_price=request.POST["ts_price"],
                              ts_ForeignKey=loggedInUser)

        return redirect('tshirtmen')
    else:
        print(new_ts.errors)
        print(new_ts.non_field_errors)
        new_ts = TshirtForm()

    return render(request, 'ivoryApp/newitem/newTshirt.html', {'new_ts': new_ts})


# your T-Shirt
def yourtshirt(request):
    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable loggedInUser
        loggedInUser = UserLoginModel.objects.get(username=request.user)
        # This will grab all of the entries for the logged in user
        personalTshirts = Tshirt.objects.filter(ts_ForeignKey=loggedInUser)
        return render(request, 'ivoryApp/youritem/yourtshirt.html', {'personalTshirts': personalTshirts})
    else:
        return render(request, 'ivoryApp/youritem/yourtshirt.html')


# edit T-Shirt
def edittshirt(request):
    return render(request, 'ivoryApp/edititem/editTshirt.html')


# delete T-Shirt
def deletetshirt(request):
    return render(request, 'ivoryApp/deleteitem/deleteTshirt.html')

############################################


# Shirt
def shirtmen(request):
    allShirts = Shirt.objects.all()
    return render(request, 'ivoryApp/item/shirtMen.html', {'allShirts': allShirts})


# new shirt
def newshirt(request):
    new_shirt = ShirtForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_shirt.is_valid():
        new_shirt = ShirtForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        Shirt.objects.create(s_title=request.POST["s_title"], s_size=request.POST["s_size"],
                             s_picture=request.FILES["s_picture"], s_price=request.POST["s_price"],
                             s_ForeignKey=loggedInUser)

        return redirect('shirtmen')
    else:
        print(new_shirt.errors)
        print(new_shirt.non_field_errors)
        new_shirt = ShirtForm()
    return render(request, 'ivoryApp/newitem/newShirt.html', {'new_shirt': new_shirt})


# your shirt
def yourshirt(request):
    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable loggedInUser
        loggedInUser = UserLoginModel.objects.get(username=request.user)
        # This will grab all of the entries for the logged in user
        personalShirts = Shirt.objects.filter(s_ForeignKey=loggedInUser)
        return render(request, 'ivoryApp/youritem/yourshirt.html', {'personalShirts': personalShirts})
    else:
        return render(request, 'ivoryApp/youritem/yourshirt.html')


# edit shirt
def editshirt(request):
    return render(request, 'ivoryApp/edititem/editShirt.html')


# delete shirt
def deleteshirt(request):
    return render(request, 'ivoryApp/deleteitem/deleteShirt.html')

############################################


# Pants
def pantsmen(request):
    allPants = Pants.objects.all()
    return render(request, 'ivoryApp/item/pantsMen.html', {'allPants': allPants})


# new pants
def newpants(request):
    new_pant = TshirtForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_pant.is_valid():
        new_pant = PantsForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        Pants.objects.create(pant_title=request.POST["pant_title"], pant_size=request.POST["pant_size"],
                             pant_picture=request.FILES["pant_picture"], pant_price=request.POST["pant_price"],
                             pant_ForeignKey=loggedInUser)

        return redirect('pantsmen')
    else:
        print(new_pant.errors)
        print(new_pant.non_field_errors)
        new_pant = PantsForm()
    return render(request, 'ivoryApp/newitem/newpants.html', {'new_pant': new_pant})


# your pants
def yourpant(request):
    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable loggedInUser
        loggedInUser = UserLoginModel.objects.get(username=request.user)
        # This will grab all of the entries for the logged in user
        personalPants = Pants.objects.filter(pant_ForeignKey=loggedInUser)
        return render(request, 'ivoryApp/youritem/yourpant.html', {'personalPants': personalPants})
    else:
        return render(request, 'ivoryApp/youritem/yourpant.html')


# edit pants
def editpants(request):
    return render(request, 'ivoryApp/edititem/editpants.html')


# delete pants
def deletepants(request):
    return render(request, 'ivoryApp/deleteitem/deletepants.html')

############################################


# Shoes
def shoesmen(request):
    allShoesMen = ShoesMen.objects.all()
    return render(request, 'ivoryApp/item/shoesMen.html', {'allShoesMen': allShoesMen})


# new men shoes
def newshoesmen(request):
    new_sm = ShoesMenForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_sm.is_valid():
        new_sm = ShoesMenForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        ShoesMen.objects.create(sm_title=request.POST["sm_title"], sm_size=request.POST["sm_size"],
                                sm_picture=request.FILES["sm_picture"], sm_price=request.POST["sm_price"],
                                sm_ForeignKey=loggedInUser)

        return redirect('shoesmen')
    else:
        print(new_sm.errors)
        print(new_sm.non_field_errors)
        new_sm = ShoesMenForm()
    return render(request, 'ivoryApp/newitem/newshoesmen.html', {'new_sm': new_sm})


# your men shoes
def yourshoesmen(request):
    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable loggedInUser
        loggedInUser = UserLoginModel.objects.get(username=request.user)
        # This will grab all of the entries for the logged in user
        personalShoesMen = ShoesMen.objects.filter(sm_ForeignKey=loggedInUser)
        return render(request, 'ivoryApp/youritem/yourshoesmen.html', {'personalShoesMen': personalShoesMen})
    else:
        return render(request, 'ivoryApp/youritem/yourshoesmen.html')


# edit men shoes
def editshoesmen(request):
    return render(request, 'ivoryApp/edititem/editshoesmen.html')


# delete men shoes
def deleteshoesmen(request):
    return render(request, 'ivoryApp/deleteitem/deleteshoesmen.html')

####################################################################################
####################################################################################

# WOMEN FUNCTIONS


def women(request):
    return render(request, 'ivoryApp/women.html')


# Dress
def dress(request):
    allDresses = Dress.objects.all()
    return render(request, 'ivoryApp/item/dress.html', {'allDresses': allDresses})


# new dress
def newdress(request):
    new_dress = DressForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_dress.is_valid():
        new_dress = ShoesMenForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        Dress.objects.create(dress_title=request.POST["dress_title"], dress_size=request.POST["dress_size"],
                             dress_picture=request.FILES["dress_picture"], dress_price=request.POST["dress_price"],
                             dress_ForeignKey=loggedInUser)

        return redirect('dress')
    else:
        print(new_dress.errors)
        print(new_dress.non_field_errors)
        new_dress = DressForm()
    return render(request, 'ivoryApp/newitem/newdress.html', {'new_dress': new_dress})


# your dress
def yourdress(request):
    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable loggedInUser
        loggedInUser = UserLoginModel.objects.get(username=request.user)
        # This will grab all of the entries for the logged in user
        personalDresses = Dress.objects.filter(dress_ForeignKey=loggedInUser)
        return render(request, 'ivoryApp/youritem/yourdress.html', {'personalDresses': personalDresses})
    else:
        return render(request, 'ivoryApp/youritem/yourdress.html')


# edit dress
def editdress(request):
    return render(request, 'ivoryApp/edititem/editdress.html')


# delete dress
def deletedress(request):
    return render(request, 'ivoryApp/deleteitem/deletedress.html')

############################################


# Bag & Jewelry
def bagjewel(request):
    allAccessories = BagJewel.objects.all()
    return render(request, 'ivoryApp/item/bagjewel.html', {'allAccessories': allAccessories})


# new accessory
def newbagjewel(request):
    new_bj = BagJewelForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_bj.is_valid():
        new_bj = BagJewelForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        BagJewel.objects.create(bj_title=request.POST["bj_title"], bj_size=request.POST["bj_size"],
                                bj_picture=request.FILES["bj_picture"], bj_price=request.POST["bj_price"],
                                bj_ForeignKey=loggedInUser)

        return redirect('bagjewel')
    else:
        print(new_bj.errors)
        print(new_bj.non_field_errors)
        new_bj = BagJewelForm()
    return render(request, 'ivoryApp/newitem/newbagjewel.html', {'new_bj': new_bj})


# your accessories
def yourbagjewel(request):
    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable loggedInUser
        loggedInUser = UserLoginModel.objects.get(username=request.user)
        # This will grab all of the entries for the logged in user
        personalAccessories = BagJewel.objects.filter(bj_ForeignKey=loggedInUser)
        return render(request, 'ivoryApp/youritem/yourbagjewel.html', {'personalAccessories': personalAccessories})
    else:
        return render(request, 'ivoryApp/youritem/yourbagjewel.html')


# edit accessory
def editbagjewel(request):
    return render(request, 'ivoryApp/edititem/editbagjewel.html')


# delete accessory
def deletebagjewel(request):
    return render(request, 'ivoryApp/deleteitem/deletebagjewel.html')

############################################


# Shoes
def shoeswomen(request):
    allShoesWomen = ShoesWomen.objects.all()
    return render(request, 'ivoryApp/item/shoesWomen.html', {'allShoesWomen': allShoesWomen})


# new women shoes
def newshoeswomen(request):
    new_sw = ShoesWomenForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_sw.is_valid():
        new_sw = ShoesWomenForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        ShoesWomen.objects.create(sw_title=request.POST["sw_title"], sw_size=request.POST["sw_size"],
                                  sw_picture=request.FILES["sw_picture"], sw_price=request.POST["sw_price"],
                                  sw_ForeignKey=loggedInUser)

        return redirect('shoeswomen')
    else:
        print(new_sw.errors)
        print(new_sw.non_field_errors)
        new_sw = ShoesWomenForm()
    return render(request, 'ivoryApp/newitem/newshoeswomen.html', {'new_sw': new_sw})


# your women shoes
def yourshoeswomen(request):
    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable loggedInUser
        loggedInUser = UserLoginModel.objects.get(username=request.user)
        # This will grab all of the entries for the logged in user
        personalShoesWomen = ShoesWomen.objects.filter(sw_ForeignKey=loggedInUser)
        return render(request, 'ivoryApp/youritem/yourshoeswomen.html', {'personalShoesWomen': personalShoesWomen})
    else:
        return render(request, 'ivoryApp/youritem/yourshoeswomen.html')


# edit women shoes
def editshoeswomen(request):
    return render(request, 'ivoryApp/edititem/editshoeswomen.html')


# delete women shoes
def deleteshoeswomen(request):
    return render(request, 'ivoryApp/deleteitem/deleteshoeswomen.html')
#################################################################################
#################################################################################


# Cart
def shoppingCart(request):
    return render(request, 'ivoryApp/shoppingCart.html')