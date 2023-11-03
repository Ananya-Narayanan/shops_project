from django.urls import path
from frontend import views

urlpatterns=[
    path('homepg/',views.homepg,name="homepg"),
    path('product/',views.product,name="product"),
    path('singlepro/<int:proid>/',views.singlepro,name="singlepro"),
    path('profilter/<cat_name>/',views.profilter,name="profilter"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('savedata/', views.savedata, name="savedata"),
    path('register/', views.register, name="register"),
    path('saveregister/', views.saveregister, name="saveregister"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('cart/', views.cart, name="cart"),
    path('savecart/', views.savecart, name="savecart"),
    path('delete_cart/<int:dataid>/', views.delete_cart, name="delete_cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('place_order/', views.place_order, name="place_order"),




]