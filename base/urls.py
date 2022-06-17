from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('profile/', views.Userprofile, name = "profile"),
    path('location-details/', views.nearbyHospitals, name="nearby-hospitals"),
    path('ajax/load-mandals/', views.loadMandals, name="ajax-load-mandals"),
    path('ajax/load-cities/', views.loadCities, name = "ajax-load-cities"),
    path('createHospitals/', views.createHospital, name="create-hospital"),
]
