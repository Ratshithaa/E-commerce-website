from django.urls import path
from . import views

urlpatterns = [

    path('', views.signup, name='home'),
    path('?/', views.main, name='main'),
    path('main/', views.main, name='main' ),
     path('insert.php', views.signup, name='signup' ),
    path('main/my_acc/',views.my_acc, name='my_acc'),
    path('main/my_acc/main/contact/', views.contact, name="contact"),
    path('main/my_acc/main/about/', views.about, name='about'),
    path('main/my_acc/main/cart', views.cart, name="cart"),
    path('main/contact/', views.contact, name='contact'),
    path('main/my_acc/main/',views.main, name='main'),
    path('main/my_acc/about/',views.about, name='about'),
    path('main/cart/',views.cart, name='cart'),
    path('main/about/',views.about, name='about'),
    path('main/cartlogreq/',views.cartlogreq, name='cartlogreq'),
    path('main/cartlogreq/login/',views.signup, name='home'),
    path('main/cartlogreq/about/', views.about, name='about'),
    path('main/cartlogreq/cart/', views.cart, name='cart'),
    path('about/my_acc', views.my_acc, name='my_acc'), 
    path('main/<str:slug>', views.collectionsview, name="collectionsview"),
    path('main/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview')

]