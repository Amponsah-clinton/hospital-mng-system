from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from . models import Patients_vitals, Laboratory_results, Antenatal_care, Notes, theater_notes, maternity_notes,emergency_notes, MFP_notes

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField( widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_OPD', 'is_A_and_C','is_Theater','is_Maternity','is_Male','is_Emergency','is_Records','is_Pharmacy','is_Laboratory')

class Patients_vitals_forms(ModelForm):
    class Meta:
        model = Patients_vitals
        fields = ( 'patient', 'pulse', 'weight', 'pressure' )
        widgets ={
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'pulse': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter pulse'}),
            'weight': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter weight'}),
            'pressure': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter pressure'}),
        }

class Lab_results_forms(ModelForm):
    class Meta:
        model = Laboratory_results
        fields = '__all__'
        widgets ={
            'patient': forms.Select(attrs={'class': 'form-control'}),
             'Results': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Results'}),
        }

class AC_vitals_forms(ModelForm):
    class Meta:
        model = Antenatal_care
        fields = ('patient','body_examination','drugs')
        widgets ={
            'patient': forms.Select(attrs={'class': 'form-control'}),
             'body_examination': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Body Examination'}),
            'drugs': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter prescribed drugs'}),
        }


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        widgets ={
            'patient': forms.Select(attrs={'class': 'form-control'}),
             'Findings': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Findings'}),
            'Drug_Prescriptions': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Drug Prescriptions'}),
        }

class theater_Record(ModelForm):
    class Meta:
        model = theater_notes
        fields = ('patient','body_examination','drugs')
        widgets ={
            'patient': forms.Select(attrs={'class': 'form-control'}),
             'Findings': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Findings'}),
            'Drug_Prescriptions': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Drug Prescriptions'}),
        }

class maternity_Record(ModelForm):
    class Meta:
        model = maternity_notes
        fields = ('patient','body_examination','drugs')
        widgets ={
            'patient': forms.Select(attrs={'class': 'form-control'}),
             'Findings': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Findings'}),
            'Drug_Prescriptions': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Drug Prescriptions'}),
        }


class emergency_Record(ModelForm):
    class Meta:
        model = emergency_notes
        fields = ('patient','body_examination','drugs')
        widgets ={
            'patient': forms.Select(attrs={'class': 'form-control'}),
             'Findings': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Findings'}),
            'Drug_Prescriptions': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Drug Prescriptions'}),
        }

class MFP_Record(ModelForm):
    class Meta:
        model = MFP_notes
        fields = ('patient','body_examination','drugs')
        widgets ={
            'patient': forms.Select(attrs={'class': 'form-control'}),
             'Findings': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Findings'}),
            'Drug_Prescriptions': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Drug Prescriptions'}),
        }










