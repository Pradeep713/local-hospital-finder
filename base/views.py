from django.shortcuts import redirect, render
from django.db.models import Q
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
        if form.is_valid():
            data = Hospital.objects.filter(
                Q(cityName_id = request.POST.get('cityName')) &
                Q(treatmentName = request.POST.get('treatmentName'))
            )
            context = {"data" : data}
            return render(request, "base/hospitals.html", context)
        else:
            print(form.errors)
            return render(request, "base/hospitals.html")
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

def createHospital(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "base/home.html")
        else:
            print(form.errors)
            return render(request, "base/home.html")
    context = {"form" : form}
    return render(request, "base/createHospital.html", context)