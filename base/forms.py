from django import forms
from django.forms import CheckboxSelectMultiple, ModelForm
from .models import Hospital, Mandal, City
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
        widgets = {
            'treatmentName' : CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['districtName'].required = True
        self.fields['mandalName'].required = True
        self.fields['cityName'].required = True
        self.fields['treatmentName'].required = False
        self.fields['cityName'].queryset = City.objects.none()
        self.fields['mandalName'].queryset = Mandal.objects.none()

        if 'districtName' in self.data:
            try:
                districtName_id= int(self.data.get('districtName'))
                self.fields['mandalName'].queryset = Mandal.objects.filter(districtName_id = districtName_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            try:
                self.fields['mandalName'].queryset = self.instance.districtName.mandalName_set.order_by('mandalName')
            except:
                pass
        
        if 'mandalName' in self.data:
            try:
                mandalName_id = int(self.data.get('mandalName'))
                self.fields['cityName'].queryset = City.objects.filter(mandalName_id = mandalName_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            try:
                self.fields['cityName'].queryset = self.instance.mandalName.cityName_set.order_by('cityName')
            except:
                pass

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # Should add choice field to UserCreationField
    CHOICES = [
        ("User", "User"),
        ("Hospital", "Hospital")
    ]
    choice = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit:True):
        user =  super(UserCreationForm, self).save(commit = False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user