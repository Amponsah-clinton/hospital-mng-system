from django.contrib import admin
from .models import User, Patients_vitals,Laboratory_results,Antenatal_care,theater_notes,maternity_notes
from django.contrib.auth.models import Group


# Register your models here.
admin.site.register(User)
admin.site.register(Patients_vitals)
admin.site.register(Antenatal_care)
admin.site.register(Laboratory_results)
admin.site.register(theater_notes)
admin.site.unregister(Group)
admin.site.register(maternity_notes)