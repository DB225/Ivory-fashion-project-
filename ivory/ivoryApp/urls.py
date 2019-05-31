from django.conf import settings
from django.urls import path, include
from . import views
from django.views.static import serve

urlpatterns = [
    # Main page
    path('', views.index, name='index'),

    # New designer
    path('newdesigner/', views.newdesigner, name='newdesigner'),

    # all items logged in user posted
    path('userEntries/', views.userEntries, name="userEntries"),

    # ROUTES FOR MEN
    path('men/', views.men, name='men'),

    # T-shirt
    path('tshirtmen/', views.tshirtmen, name='tshirtmen'),
    path('newtshirt/', views.newtshirt, name='newtshirt'),
    path('readtshirt/<int:ts_id>/', views.readtshirt, name='readtshirt'),
    path('edittshirt/<int:ts_id>/', views.edittshirt, name='edittshirt'),
    path('deletetshirt/<int:deletets_id>/', views.deletetshirt, name='deletetshirt'),

    # Shirt
    path('shirtmen/', views.shirtmen, name='shirtmen'),
    path('newshirt/', views.newshirt, name='newshirt'),
    path('readshirt/<int:s_id>/', views.readshirt, name='readshirt'),
    path('editshirt/<int:s_id>/', views.editshirt, name='editshirt'),
    path('deleteshirt/<int:deletesh_id>/', views.deleteshirt, name='deleteshirt'),

    # Pants
    path('pantsmen/', views.pantsmen, name='pantsmen'),
    path('newpants/', views.newpants, name='newpants'),
    path('readpants/<int:p_id>/', views.readpants, name='readpants'),
    path('editpants/<int:p_id>/', views.editpants, name='editpants'),
    path('deletepants/<int:deletep_id>/', views.deletepants, name='deletepants'),

    # Shoes
    path('shoesmen/', views.shoesmen, name='shoesmen'),
    path('newshoesmen/', views.newshoesmen, name='newshoesmen'),
    path('readshoesmen/<int:shoes_id>/', views.readshoesmen, name='readshoesmen'),
    path('editshoesmen/<int:shoes_id>/', views.editshoesmen, name='editshoesmen'),
    path('deleteshoesmen/<int:deleteshoes_id>/', views.deleteshoesmen, name='deleteshoesmen'),
    #####################################################################

    # ROUTES FOR WOMEN
    path('women/', views.women, name='women'),

    # Dress
    path('dress/', views.dress, name='dress'),
    path('newdress/', views.newdress, name='newdress'),
    path('readdress/<int:dr_id>/', views.readdress, name='readdress'),
    path('editdress/<int:dr_id>/', views.editdress, name='editdress'),
    path('deletedress/<int:deletedr_id>/', views.deletedress, name='deletedress'),

    # Bag & Jewelry
    path('bagjewel/', views.bagjewel, name='bagjewel'),
    path('newbagjewel/', views.newbagjewel, name='newbagjewel'),
    path('readbagjewel/<int:acc_id>/', views.readbagjewel, name='readbagjewel'),
    path('editbagjewel/<int:acc_id>/', views.editbagjewel, name='editbagjewel'),
    path('deletebagjewel/<int:deleteacc_id>/', views.deletebagjewel, name='deletebagjewel'),

    # Shoes
    path('shoeswomen/', views.shoeswomen, name='shoeswomen'),
    path('newshoeswomen/', views.newshoeswomen, name='newshoeswomen'),
    path('readshoeswomen/<int:swomen_id>/', views.readshoeswomen, name='readshoeswomen'),
    path('editshoeswomen/<int:swomen_id>/', views.editshoeswomen, name='editshoeswomen'),
    path('deleteshoeswomen/<int:deleteswomen_id>/', views.deleteshoeswomen, name='deleteshoeswomen'),

    # Cart
    path('shoppingCart/', views.shoppingCart, name='shoppingCart'),

    # the path for the images
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
