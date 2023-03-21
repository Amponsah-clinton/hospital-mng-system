from django.forms import ModelForm
from .models import inquiry, AddRecord, contact_us,appointment
from django import forms

class inquiryForm(ModelForm):
    class Meta:
        model = inquiry
        fields ="__all__"

class RecordForm(ModelForm):
    class Meta:
        model = AddRecord
        fields ="__all__"

class contact_us_form(ModelForm):
    class Meta:
        model = contact_us
        fields = "__all__"

class appointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        ordering =['-date']
        fields = "__all__"
        widgets ={
            'Doctor': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter name'}),
             'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter phone number'}),
            'complains': forms.Textarea (attrs={'class': 'form-control','placeholder':'Enter complains'}),
        }





