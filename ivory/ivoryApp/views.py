from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from django.db.models import Q


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
    # out_of_smalls = Tshirt.objects.filter(ts_size='S').count() == 5
    form = MyForm()
    allTshirts = Tshirt.objects.all()
    context = {
        'allTshirts': allTshirts,
        'form': form,
        # 'out_of_smalls': out_of_smalls
    }
    return render(request, 'ivoryApp/item/tShirtMen.html', context)


# new T-Shirt
def newtshirt(request):
    new_ts = TshirtForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_ts.is_valid():
        new_ts = TshirtForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        Tshirt.objects.create(ts_title=request.POST["ts_title"], ts_picture=request.FILES["ts_picture"],
                              ts_price=request.POST["ts_price"], ts_ForeignKey=loggedInUser)

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
def edittshirt(request, ts_id):
    edit_tshirt = get_object_or_404(Tshirt, pk=ts_id)
    editedTshirt = TshirtForm(request.POST or None, instance=edit_tshirt)
    if editedTshirt.is_valid():
        editedTshirt.save()
        return redirect('tshirtmen')
    return render(request, 'ivoryApp/edititem/editTshirt.html', {'editedTshirt': editedTshirt})


# delete T-Shirt
def deletetshirt(request, deletets_id):
    delete_tshirt = get_object_or_404(Tshirt, pk=deletets_id)
    if request.method == 'POST':
        delete_tshirt.delete()
        redirect('tshirtmen')
    return render(request, 'ivoryApp/deleteitem/deleteTshirt.html', {'delete_tshirt': delete_tshirt})

############################################


# Shirt
def shirtmen(request):
    form = MyForm()
    allShirts = Shirt.objects.all()
    return render(request, 'ivoryApp/item/shirtMen.html', {'allShirts': allShirts, 'form': form})


# new shirt
def newshirt(request):
    new_shirt = ShirtForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_shirt.is_valid():
        new_shirt = ShirtForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        Shirt.objects.create(s_title=request.POST["s_title"], s_picture=request.FILES["s_picture"],
                             s_price=request.POST["s_price"], s_ForeignKey=loggedInUser)

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
def editshirt(request, s_id):
    edit_shirt = get_object_or_404(Shirt, pk=s_id)
    editedShirt = ShirtForm(request.POST or None, instance=edit_shirt)
    if editedShirt.is_valid():
        editedShirt.save()
        return redirect('shirtmen')
    return render(request, 'ivoryApp/edititem/editShirt.html', {'editedShirt': editedShirt})


# delete shirt
def deleteshirt(request, deletesh_id):
    delete_shirt = get_object_or_404(Shirt, pk=deletesh_id)
    if request.method == 'POST':
        delete_shirt.delete()
        redirect('shirtmen')
    return render(request, 'ivoryApp/deleteitem/deleteShirt.html', {'delete_shirt': delete_shirt})

############################################


# Pants
def pantsmen(request):
    form = MyForm()
    allPants = Pants.objects.all()
    return render(request, 'ivoryApp/item/pantsMen.html', {'allPants': allPants, 'form': form})


# new pants
def newpants(request):
    new_pant = PantsForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_pant.is_valid():
        new_pant = PantsForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        Pants.objects.create(pant_title=request.POST["pant_title"], pant_picture=request.FILES["pant_picture"],
                             pant_price=request.POST["pant_price"], pant_ForeignKey=loggedInUser)

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
def editpants(request, p_id):
    edit_pant = get_object_or_404(Pants, pk=p_id)
    editedPant = PantsForm(request.POST or None, instance=edit_pant)
    if editedPant.is_valid():
        editedPant.save()
        return redirect('pantsmen')
    return render(request, 'ivoryApp/edititem/editpants.html', {'editedPant': editedPant})


# delete pants
def deletepants(request, deletep_id):
    delete_pant = get_object_or_404(Pants, pk=deletep_id)
    if request.method == 'POST':
        delete_pant.delete()
        redirect('pantsmen')
    return render(request, 'ivoryApp/deleteitem/deletepants.html', {'delete_pant': delete_pant})

############################################


# Shoes
def shoesmen(request):
    form = MyForm()
    allShoesMen = ShoesMen.objects.all()
    return render(request, 'ivoryApp/item/shoesMen.html', {'allShoesMen': allShoesMen, 'form': form})


# new men shoes
def newshoesmen(request):
    new_sm = ShoesMenForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_sm.is_valid():
        new_sm = ShoesMenForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        ShoesMen.objects.create(sm_title=request.POST["sm_title"], sm_picture=request.FILES["sm_picture"],
                                sm_price=request.POST["sm_price"], sm_ForeignKey=loggedInUser)

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
def editshoesmen(request, smen_id):
    edit_sm = get_object_or_404(ShoesMen, pk=smen_id)
    editedSm = ShoesMenForm(request.POST or None, instance=edit_sm)
    if editedSm.is_valid():
        editedSm.save()
        return redirect('shoesmen')
    return render(request, 'ivoryApp/edititem/editshoesmen.html', {'editedSm': editedSm})


# delete men shoes
def deleteshoesmen(request, deletesmen_id):
    delete_sm = get_object_or_404(ShoesMen, pk=deletesmen_id)
    if request.method == 'POST':
        delete_sm.delete()
        redirect('shoesmen')
    return render(request, 'ivoryApp/deleteitem/deleteshoesmen.html', {'delete_sm': delete_sm})

####################################################################################
####################################################################################

# WOMEN FUNCTIONS


def women(request):
    return render(request, 'ivoryApp/women.html')


# Dress
def dress(request):
    form = MyForm()
    allDresses = Dress.objects.all()
    return render(request, 'ivoryApp/item/dress.html', {'allDresses': allDresses, 'form': form})


# new dress
def newdress(request):
    new_dress = DressForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_dress.is_valid():
        new_dress = DressForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        Dress.objects.create(dress_title=request.POST["dress_title"], dress_picture=request.FILES["dress_picture"],
                             dress_price=request.POST["dress_price"], dress_ForeignKey=loggedInUser)

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
def editdress(request, dr_id):
    edit_dress = get_object_or_404(Dress, pk=dr_id)
    editedDress = DressForm(request.POST or None, instance=edit_dress)
    if editedDress.is_valid():
        editedDress.save()
        return redirect('dress')
    return render(request, 'ivoryApp/edititem/editdress.html', {'editedDress': editedDress})


# delete dress
def deletedress(request, deletedr_id):
    delete_dress = get_object_or_404(Dress, pk=deletedr_id)
    if request.method == 'POST':
        delete_dress.delete()
        redirect('dress')
    return render(request, 'ivoryApp/deleteitem/deletedress.html', {'delete_dress': delete_dress})

############################################


# Bag & Jewelry
def bagjewel(request):
    form = MyForm()
    allAccessories = BagJewel.objects.all()
    return render(request, 'ivoryApp/item/bagjewel.html', {'allAccessories': allAccessories, 'form': form})


# new accessory
def newbagjewel(request):
    new_bj = BagJewelForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_bj.is_valid():
        new_bj = BagJewelForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        BagJewel.objects.create(bj_title=request.POST["bj_title"], bj_picture=request.FILES["bj_picture"],
                                bj_price=request.POST["bj_price"], bj_ForeignKey=loggedInUser)

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
def editbagjewel(request, acc_id):
    edit_acc = get_object_or_404(BagJewel, pk=acc_id)
    editedAcc = BagJewelForm(request.POST or None, instance=edit_acc)
    if editedAcc.is_valid():
        editedAcc.save()
        return redirect('bagjewel')
    return render(request, 'ivoryApp/edititem/editbagjewel.html', {'editedAcc': editedAcc})


# delete accessory
def deletebagjewel(request, deleteacc_id):
    delete_acc = get_object_or_404(BagJewel, pk=deleteacc_id)
    if request.method == 'POST':
        delete_acc.delete()
        redirect('bagjewel')
    return render(request, 'ivoryApp/deleteitem/deletebagjewel.html', {'delete_acc': delete_acc})

############################################


# Shoes
def shoeswomen(request):
    form = MyForm()
    allShoesWomen = ShoesWomen.objects.all()
    return render(request, 'ivoryApp/item/shoesWomen.html', {'allShoesWomen': allShoesWomen, 'form': form})


# new women shoes
def newshoeswomen(request):
    new_sw = ShoesWomenForm(request.POST or None)
    print(request.POST)

    if request.method == 'POST' or new_sw.is_valid():
        new_sw = ShoesWomenForm(request.POST, request.FILES)
        loggedInUser = get_object_or_404(UserLoginModel, username=request.user)
        ShoesWomen.objects.create(sw_title=request.POST["sw_title"], sw_picture=request.FILES["sw_picture"],
                                  sw_price=request.POST["sw_price"], sw_ForeignKey=loggedInUser)

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
def editshoeswomen(request, swomen_id):
    edit_sw = get_object_or_404(ShoesWomen, pk=swomen_id)
    editedSw = ShoesWomenForm(request.POST or None, instance=edit_sw)
    if editedSw.is_valid():
        editedSw.save()
        return redirect('shoeswomen')
    return render(request, 'ivoryApp/edititem/editshoeswomen.html', {'editedSw': editedSw})


# delete women shoes
def deleteshoeswomen(request, deleteswomen_id):
    delete_sw = get_object_or_404(ShoesWomen, pk=deleteswomen_id)
    if request.method == 'POST':
        delete_sw.delete()
        redirect('shoeswomen')
    return render(request, 'ivoryApp/deleteitem/deleteshoeswomen.html', {'delete_sw': delete_sw})
#################################################################################
#################################################################################


# find informations through the search bar
def search_ts(request):
    form = MyForm()
    makeSearch = request.POST['mySearch']
    research_ts = Tshirt.objects.filter(Q(ts_title__startswith=makeSearch))
    context = {
        'research_ts': research_ts,
        'form': form
    }
    return render(request, 'ivoryApp/search/search_ts.html', context)


def search_s(request):
    form = MyForm()
    makeSearch = request.POST['mySearch']
    research_s = Shirt.objects.filter(Q(s_title__startswith=makeSearch))
    return render(request, 'ivoryApp/search/search_s.html', {'research_s': research_s, 'form': form})


def search_pant(request):
    form = MyForm()
    makeSearch = request.POST['mySearch']
    research_pant = Pants.objects.filter(Q(pant_title__startswith=makeSearch))
    return render(request, 'ivoryApp/search/search_pant.html', {'research_pant': research_pant, 'form': form})


def search_sm(request):
    form = MyForm()
    makeSearch = request.POST['mySearch']
    research_sm = ShoesMen.objects.filter(Q(sm_title__startswith=makeSearch))
    return render(request, 'ivoryApp/search/search_sm.html', {'research_sm': research_sm, 'form': form})


def search_dress(request):
    form = MyForm()
    makeSearch = request.POST['mySearch']
    research_dress = Dress.objects.filter(Q(dress_title__startswith=makeSearch))
    return render(request, 'ivoryApp/search/search_dress.html', {'research_dress': research_dress, 'form': form})


def search_bj(request):
    form = MyForm()
    makeSearch = request.POST['mySearch']
    research_bj = BagJewel.objects.filter(Q(bj_title__startswith=makeSearch))
    return render(request, 'ivoryApp/search/search_bj.html', {'research_bj': research_bj, 'form': form})


def search_sw(request):
    form = MyForm()
    makeSearch = request.POST['mySearch']
    research_sw = ShoesWomen.objects.filter(Q(sw_title__startswith=makeSearch))
    return render(request, 'ivoryApp/search/search_sw.html', {'research_sw': research_sw, 'form': form})


# Cart
def shoppingCart(request):
    return render(request, 'ivoryApp/shoppingCart.html')
