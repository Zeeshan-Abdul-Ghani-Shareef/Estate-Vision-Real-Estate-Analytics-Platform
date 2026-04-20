from django.urls import path

from . import views
from django.conf.urls.static import static

urlpatterns = [
      
    path("", views.index, name="index"),

    path('index/', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('product/<int:id>', views.product, name='product'),

    path('productDetail/<int:id>', views.productDetail, name='productDetail'),

    path('cart/', views.cart, name='cart'),

    path('checkout/', views.checkout, name='checkout'),

    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('cart/update/<int:product_id>/', views.update_to_cart, name='update_to_cart'),

    path('calculator/', views.calculator, name='calculator'),

    path('marksheet/', views.marksheet, name='marksheet'),

    path('tablegen/', views.tablegen, name='tablegen'),

    #---------------login and auth----------------
    path('login/', views.login_user, name='login_user'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout_user'),

    path('register/', views.Register_Customer, name='register'),

    path('place_order/', views.place_order, name='place_order'),

    path('realEstateSearch/', views.realEstateSearch, name='realEstateSearch'),
   
    path("realEstateSearch/<str:country_name>/", views.realEstateSearch, name="realEstateSearchByCountry"),


    path('realEstateGraph/', views.realEstateGraph, name='realEstateGraph'),
    
    path('realEstateGraph2/', views.realEstateGraph2, name='realEstateGraph2'),
    
    path("chatbot/", views.chatbot, name="chat_api"),  # <-- name matches frontend

    path("get-city-location/", views.get_city_location, name="get_city_location"),
    
] 
