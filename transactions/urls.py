"""
URL configuration for budget project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views
from .views import kategorie_formularz

urlpatterns = [
    path('', views.budzet, name='domowa'),
    path('konto/Budżet.html', views.budzet),
    path('konto/strona_opcja.html', views.strona_opcja),
    path('konto/strona_rejestracja.html', views.register_request, name='register'),
    path('konto/strona_konto.html', views.login_request),
    path('przychody_dochody/strona_przychody_dochody.html', views.przychody_dochody, name='przychody_dochody'),
    path('kategorie/strona_kategorie.html', views.kategorie_formularz),
    path('transakcje/strona_transakcje.html', views.transakcje_formularz),
    path('registration_result/Budżet.html',views.budzet),
    path('login_result/Budżet.html',views.budzet),
    #path("", views.homepage, name="homepage"), #Adams
    #path("register", views.register_request, name="register"), #Adams
    path("registration_result/<str:registration_success>", views.registration_result, name="registration_result"), #Adams
    path("login_result/<str:login_success>", views.login_result, name="login_result"), #Adams
    #path("login", views.login_request, name="login"), #Adams,
    path('transakcje/statystyki.html', views.statystyki, name='statystyki'),
    path('transakcje/wykresy.html', views.wykresy, name='wykresy'),
    path('transakcje/<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('transakcje/<int:pk>/remove/', views.transaction_remove, name='transaction_remove'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('kategorie/category_list.html', views.category_list, name='category_list'),
    path('category/<int:pk>/remove/', views.category_remove, name='category_remove'),

]
