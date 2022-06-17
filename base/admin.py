from django.contrib import admin
from .models import District, Hospital, Mandal, City, Treatement

admin.site.register(District)
admin.site.register(Mandal)
admin.site.register(City)
admin.site.register(Hospital)
admin.site.register(Treatement)