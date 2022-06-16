from django.forms import ModelForm
from .models import Hospital, District, Mandal, City

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
        # exclude = ['hospitalName']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cityName'].queryset = City.objects.none()
        self.fields['mandalName'].queryset = Mandal.objects.none()

        if 'districtName' in self.data:
            try:
                districtName_id= int(self.data.get('districtname'))
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
                self.fields['mandalName'].queryset = City.objects.filter(mandalName_id = mandalName_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            try:
                self.fields['cityName'].queryset = self.instance.mandalName.cityName_set.order_by('cityName')
            except:
                pass