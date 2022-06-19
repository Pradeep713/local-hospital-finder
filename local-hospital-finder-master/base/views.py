from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from base.models import City, Mandal, Hospital
from .forms import HospitalForm
from django.contrib import messages

# Create your views here.

def home(request):
    context = {"text" : "Working"}
    return render(request, "base/home.html", context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    page = 'login'
    if request.method == 'POST':
        userExist = True
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            userExist = False
            messages.error(request, "User doesn't exist")        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        elif userExist:
            messages.error(request, "Username or Password do not match")
    context = {'page' : page}
    return render(request, "base/login-register.html", context)

def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occured during registration")
    context = {'page' : page, 'form': form}
    return render(request, "base/login-register.html", context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url= '/login')
def userProfile(request):
    context = {"user" : request.user}
    return render(request, "base/userProfile.html", context)

def nearbyHospitals(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            data = list(Hospital.objects.filter(
                Q(cityName_id = request.POST.get('cityName')) &
                Q(treatmentName = request.POST.get('treatmentName'))
            ))
            if not data:
                data = list(Hospital.objects.filter(
                    Q(cityName_id = request.POST.get('mandalName')) &
                    Q(treatmentName = request.POST.get('treatmentName'))
                ))
                if not data:
                    data = list(Hospital.objects.filter(
                        Q(cityName_id = request.POST.get('districtName')) &
                        Q(treatmentName = request.POST.get('treatmentName'))
                    ))
                    if not data:
                        data = "Not available hospitals in your district. Try single treatment at a time if you choose many"
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

@login_required(login_url= '/login')
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