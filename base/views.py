from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
from django.shortcuts import redirect, render

from base.models import City, Mandal, Hospital
from .forms import HospitalForm

# Create your views here.

def home(request):
    context = {"text" : "Working"}
    return render(request, "base/home.html", context)

def Userprofile(request):
    pass

def nearbyHospitals(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        data = Hospital.objects.filter(cityName_id = request.POST.get('cityName'))
        context = {"data" : data}
        print(data)
        return render(request, "base/hospitals.html", context)
    context = {"form" : form}
    return render(request, "base/nearbyhospitals.html", context)

def loadMandals(request):
    district_id = request.GET.get('districtId')
    mandals = Mandal.objects.filter(districtName_id = district_id)
    context = {"data" : mandals, "isCity" : False}
    return render(request, "base/dropdownlist.html", context)

def loadCities(request):
    mandal_id = request.GET.get('mandalId')
    cities = City.objects.filter(mandalName_id = mandal_id)
    context = {"data" : cities, "isCity" : True}
    return render(request, "base/dropdownlist.html", context)

def loadHospitals(request):
    pass