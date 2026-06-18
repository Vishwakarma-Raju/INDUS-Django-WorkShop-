from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage),
    path('home',views.homepage),
    path('about',views.aboutpage),
    path('contact',views.contactpage),
    path('ToyShop',views.ToyShoppage),
    path('contactprocess',views.contactprocess),
    path('homeprocess',views.homeprocess),
    path('saveSession',views.saveSessionData),
    path('getSession',views.getSessionData),
    path('deleteSession',views.deleteSessionData),
    path('getSession2',views.getSessionData2),

# login page
    
    path('login',views.loginPage),
    path('loginprocess',views.loginProcess),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
    path('maildemo',views.mailsenddemo),

]