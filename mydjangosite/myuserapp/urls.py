from django.urls import path
from . import views



urlpatterns = [
    path('',views.homepage),
    path('home',views.homepage),
    path('about',views.aboutpage),
    path('contact',views.contactpage),
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
    path('process',views.mailsendprocess),
    path('senddetail',views.senddetail),

    # Get details
    path('addstudent',views.addstudentform),
    path('addstudentformprocess',views.addstudentformprocess),


    
    
    path('addcategory',views.addcategory ),
    path('displaycategory',views.displaycategory ),
    path('deletecategory/<int:id>',views.deletecategory ),
    path('editcategory/<int:id>',views.editcategory ),
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='logout'),
    path('displayproductApi',views.displayproductApi),
    path('product/',views.displayproduct)


]