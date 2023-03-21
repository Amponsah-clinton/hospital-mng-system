from django.contrib import admin
from .models import inquiry,AddRecord,contact_us,Doctor,appointment
# Register your models here.

admin.site.register(inquiry)
admin.site.register(contact_us)
admin.site.register(AddRecord)
admin.site.register(Doctor)
admin.site.register(appointment)

