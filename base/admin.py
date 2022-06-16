from django.contrib import admin
from .models import District, Hospital, Mandal, City

admin.site.register(District)
admin.site.register(Mandal)
admin.site.register(City)
admin.site.register(Hospital)