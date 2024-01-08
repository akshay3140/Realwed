from django.urls import path
from app import views

urlpatterns = [
    path('',views.fun,name='fun'),
    path('login',views.login,name='login'),
    path('indexpage',views.indexpage,name='indexpage'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('photographer',views.photographer,name='photographer'),
    path('venues',views.venues,name='venues'),
    path('cake',views.cake,name='cake'),
    path('logout',views.logout,name='logout'),
    path('venue_detail/<int:id>',views.venue_detail,name='venue_detail'),
    path('photographer_detail/<int:id>',views.photographer_detail,name='photographer_detail'),
    path('cake_detail/<int:id>',views.cake_detail,name='cake_detail'),
    path('search',views.search,name='search'),
    path('searchcake',views.searchcake,name='searchcake'),
    path('searchphoto',views.searchphoto,name='searchphoto'),
    path('beautision',views.beautision,name='beautision'),
    path('beauticion/<int:id>',views.beauticion,name='beauticion'),
    path('searchbeauticion',views.searchbeauticion,name='searchbeauticion')
]