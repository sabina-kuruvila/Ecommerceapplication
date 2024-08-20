from django.urls import path
from shop import views


urlpatterns = [
    path('',views.base,name= "base"),
    path('home/',views.home,name= "home"),
    path('products/',views.product_list,name= "product_list"),
    path('contact/',views.contact,name= "contact"),
    path('products/<int:id>',views.product_detail,name= "product_detail"),
    path('about/',views.about,name= "about"),
]