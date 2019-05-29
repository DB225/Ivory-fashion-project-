from django.urls import path
from . import views

urlpatterns = [
    # Main page
    path('', views.index, name='index'),

    # Men routes
    path('men/', views.men, name='men'),
    path('tshirtmen', views.tshirtmen, name='tshirtmen'),
    path('shirtmen', views.shirtmen, name='shirtmen'),
    path('pantsmen/', views.pantsmen, name='pantsmen'),
    path('shoesmen/', views.shoesmen, name='shoesmen'),

    # Women routes
    path('women/', views.women, name='women'),
    path('dress/', views.dress, name='dress'),
    path('bagjewel/', views.bagjewel, name='bagjewel'),
    path('shoeswomen/', views.shoeswomen, name='shoeswomen'),

    # Boys routes
    path('boys/', views.boys, name='boys'),
    # path('boys/', views.boys, name='boys'),
    # path('boys/', views.boys, name='boys'),
    # path('boys/', views.boys, name='boys'),

    # Girls routes
    path('girls/', views.girls, name='girls'),
    # path('girls/', views.girls, name='girls'),
    # path('girls/', views.girls, name='girls'),
    # path('girls/', views.girls, name='girls'),

    # Cart
    path('shoppingCart/', views.shoppingCart, name='shoppingCart'),
]