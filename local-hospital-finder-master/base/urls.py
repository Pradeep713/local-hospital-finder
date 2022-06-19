from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('location-details/', views.nearbyHospitals, name="nearby-hospitals"),
    path('ajax/load-mandals/', views.loadMandals, name="ajax-load-mandals"),
    path('ajax/load-cities/', views.loadCities, name = "ajax-load-cities"),
    path('createHospitals/', views.createHospital, name="create-hospital"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('profile/', views.userProfile, name = "profile"),
]
