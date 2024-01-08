from django.urls import path
from vender import views

urlpatterns = [
    path('reg',views.reg,name='reg'),
    path('login1',views.login1,name='login1'),
    path('logout1',views.logout1,name='logout1'),
    path('coupleprofile',views.coupleprofile,name='coupleprofile'),
    path('coupledashboard',views.coupledashboard,name='coupledashboard'),
    # path('coupletodolist',views.coupletodolist,name='coupletodolist'),
    path('viewvenue',views.viewvenue,name='viewvenue'),
    path('coupleguest',views.coupleguest,name='coupleguest'),
    # path('photographertodolist',views.photographertodolist,name='photographertodolist'),
    path('viewphotographer',views.viewphotographer,name='viewphotographer'),
    path('photographerguests',views.photographerguests,name='photographerguests'),
    # path('catererstodolist',views.caterestodolist,name='catererstodolist'),
    path('viewcaterers',views.viewcaterers,name='viewcaterers'),
    path('caterersguest',views.caterersguests,name='caterersguest'),
    # path('beauticiontodolist',views.beauticiontodolist,name='beauticiontodolist'),
    path('beauticionguest',views.beauticionguest,name='beauticionguest'),
    path('viewbeauticion',views.viewbeauticion,name='viewbeauticion')
    
    
]