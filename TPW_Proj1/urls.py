"""TPW_Proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('find/', views.contact, name='find'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sendEmail/', views.sendEmail, name='sendemail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('successregister/', views.successregister, name="successregister"),
    path('infoItem', views.getItem, name='infoitem'),
    path('search', views.search, name='search'),
    path('profile/', views.getProfile, name="profile"),
    path('profileedit/', views.editprofile, name="profileedit"),
    path('updateProfile', views.updateProfile, name="updateProfile"),
    path('adminPanel/', views.painel, name='adminpanel'),
    path('additem/', views.addProducts, name='additem'),
    path('processadd', views.processAdd, name='processadd'),
    path('deleteitem/', views.removeProducts, name='deleteitem'),
    path('edititem/', views.editProducts, name='edititem'),
    path('processedit', views.processEdit, name='processedit'),
    path('searchadmin/', views.searchAdmin, name='searchadmin'),
    path('addcart', views.addCart, name="addcart"),
    path('removecart', views.removeCart, name="removecart"),
    path('shoppingcart/', views.shoppingCart, name="shoppingcart"),
    path('checkout/', views.checkout, name="checkout"),
    path('boughtlist/', views.bought, name="boughtlist"),
    path('boughtSearch', views.boughtSearch, name="boughtSearch"),
    path('boughtlistAdmin', views.boughtAdmin, name="boughtlistAdmin"),
    path('boughtSearchAdmin', views.boughtSearchAdmin, name="boughtSearchAdmin"),
    path('buyitem', views.buyItem, name='buyitem')
]
