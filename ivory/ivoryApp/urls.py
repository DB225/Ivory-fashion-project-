from django.conf import settings
from django.urls import path, include
from . import views
from django.views.static import serve

urlpatterns = [
    # Main page
    path('', views.index, name='index'),

    # ROUTES FOR MEN
    path('men/', views.men, name='men'),

    # T-shirt
    path('tshirtmen', views.tshirtmen, name='tshirtmen'),
    path('newtshirt', views.newtshirt, name='newtshirt'),
    path('readtshirt', views.readtshirt, name='readtshirt'),
    path('edittshirt', views.edittshirt, name='edittshirt'),
    path('deletetshirt', views.deletetshirt, name='deletetshirt'),

    # Shirt
    path('shirtmen', views.shirtmen, name='shirtmen'),
    path('newshirt', views.newshirt, name='newshirt'),
    path('readshirt', views.readshirt, name='readshirt'),
    path('editshirt', views.editshirt, name='editshirt'),
    path('deleteshirt', views.deleteshirt, name='deleteshirt'),

    # Pants
    path('pantsmen/', views.pantsmen, name='pantsmen'),
    path('newpants/', views.newpants, name='newpants'),
    path('readpants/', views.readpants, name='readpants'),
    path('editpants/', views.editpants, name='editpants'),
    path('deletepants/', views.deletepants, name='deletepants'),

    # Shoes
    path('shoesmen/', views.shoesmen, name='shoesmen'),
    path('newshoesmen/', views.newshoesmen, name='newshoesmen'),
    path('readshoesmen/', views.readshoesmen, name='readshoesmen'),
    path('editshoesmen/', views.editshoesmen, name='editshoesmen'),
    path('deleteshoesmen/', views.deleteshoesmen, name='deleteshoesmen'),
    #####################################################################

    # ROUTES FOR WOMEN
    path('women/', views.women, name='women'),

    # Dress
    path('dress/', views.dress, name='dress'),
    path('newdress/', views.newdress, name='newdress'),
    path('readdress/', views.readdress, name='readdress'),
    path('editdress/', views.editdress, name='editdress'),
    path('deletedress/', views.deletedress, name='deletedress'),

    # Bag & Jewelry
    path('bagjewel/', views.bagjewel, name='bagjewel'),
    path('newbagjewel/', views.newbagjewel, name='newbagjewel'),
    path('readbagjewel/', views.readbagjewel, name='readbagjewel'),
    path('editbagjewel/', views.editbagjewel, name='editbagjewel'),
    path('deletebagjewel/', views.deletebagjewel, name='deletebagjewel'),

    # Shoes
    path('shoeswomen/', views.shoeswomen, name='shoeswomen'),
    path('newshoeswomen/', views.newshoeswomen, name='newshoeswomen'),
    path('readshoeswomen/', views.readshoeswomen, name='readshoeswomen'),
    path('editshoeswomen/', views.editshoeswomen, name='editshoeswomen'),
    path('deleteshoeswomen/', views.deleteshoeswomen, name='deleteshoeswomen'),

    # Cart
    path('shoppingCart/', views.shoppingCart, name='shoppingCart'),

    # the path for the images
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
