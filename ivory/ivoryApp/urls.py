from django.conf import settings
from django.urls import path, include
from . import views
from django.views.static import serve

urlpatterns = [
    # Main page
    path('', views.index, name='index'),

    # New designer
    path('newdesigner/', views.newdesigner, name='newdesigner'),

    # ROUTES FOR MEN
    path('men/', views.men, name='men'),

    # T-shirt
    path('tshirtmen/', views.tshirtmen, name='tshirtmen'),
    path('newtshirt/', views.newtshirt, name='newtshirt'),
    path('yourtshirt/', views.yourtshirt, name='yourtshirt'),
    path('edittshirt/<int:ts_id>/', views.edittshirt, name='edittshirt'),
    path('deletetshirt/<int:deletets_id>/', views.deletetshirt, name='deletetshirt'),

    # Shirt
    path('shirtmen/', views.shirtmen, name='shirtmen'),
    path('newshirt/', views.newshirt, name='newshirt'),
    path('yourshirt/', views.yourshirt, name='yourshirt'),
    path('editshirt/<int:s_id>/', views.editshirt, name='editshirt'),
    path('deleteshirt/<int:deletesh_id>/', views.deleteshirt, name='deleteshirt'),

    # Pants
    path('pantsmen/', views.pantsmen, name='pantsmen'),
    path('newpants/', views.newpants, name='newpants'),
    path('yourpant/', views.yourpant, name='yourpant'),
    path('editpants/<int:p_id>/', views.editpants, name='editpants'),
    path('deletepants/<int:deletep_id>/', views.deletepants, name='deletepants'),

    # Shoes
    path('shoesmen/', views.shoesmen, name='shoesmen'),
    path('newshoesmen/', views.newshoesmen, name='newshoesmen'),
    path('yourshoesmen/', views.yourshoesmen, name='yourshoesmen'),
    path('editshoesmen/<int:smen_id>/', views.editshoesmen, name='editshoesmen'),
    path('deleteshoesmen/<int:deletesmen_id>/', views.deleteshoesmen, name='deleteshoesmen'),
    #####################################################################

    # ROUTES FOR WOMEN
    path('women/', views.women, name='women'),

    # Dress
    path('dress/', views.dress, name='dress'),
    path('newdress/', views.newdress, name='newdress'),
    path('yourdress/', views.yourdress, name='yourdress'),
    path('editdress/<int:dr_id>/', views.editdress, name='editdress'),
    path('deletedress/<int:deletedr_id>/', views.deletedress, name='deletedress'),

    # Bag & Jewelry
    path('bagjewel/', views.bagjewel, name='bagjewel'),
    path('newbagjewel/', views.newbagjewel, name='newbagjewel'),
    path('yourbagjewel/', views.yourbagjewel, name='yourbagjewel'),
    path('editbagjewel/<int:acc_id>/', views.editbagjewel, name='editbagjewel'),
    path('deletebagjewel/<int:deleteacc_id>/', views.deletebagjewel, name='deletebagjewel'),

    # Shoes
    path('shoeswomen/', views.shoeswomen, name='shoeswomen'),
    path('newshoeswomen/', views.newshoeswomen, name='newshoeswomen'),
    path('yourshoeswomen/', views.yourshoeswomen, name='yourshoeswomen'),
    path('editshoeswomen/<int:swomen_id>/', views.editshoeswomen, name='editshoeswomen'),
    path('deleteshoeswomen/<int:deleteswomen_id>/', views.deleteshoeswomen, name='deleteshoeswomen'),


    # the pages of the result of search via the search bar
    path('search_ts/', views.search_ts, name="search_ts"),
    path('search_s/', views.search_s, name="search_s"),
    path('search_pant/', views.search_pant, name="search_pant"),
    path('search_sm/', views.search_sm, name="search_sm"),
    path('search_dress/', views.search_dress, name="search_dress"),
    path('search_bj/', views.search_bj, name="search_bj"),
    path('search_sw/', views.search_sw, name="search_sw"),

    # Cart
    path('shoppingCart/', views.shoppingCart, name='shoppingCart'),

    # the path for the images
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
