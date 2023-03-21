from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import AddRecord
from .forms import Patients_vitals_forms,Lab_results_forms, AC_vitals_forms,NotesForm,theater_Record,maternity_Record, emergency_Record,MFP_Record
from . models import Patients_vitals, Notes
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_OPD:
                login(request, user)
                return redirect('opd')
            elif user is not None and user.is_A_and_C:
                login(request, user)
                return redirect('AC')
            elif user is not None and user.is_Theater:
                login(request, user)
                return redirect('theater')
            elif user is not None and user.is_Maternity:
                login(request, user)
                return redirect('maternity')     
            elif user is not None and user.is_Male:
                login(request, user)
                return redirect('MFP')
            elif user is not None and user.is_Emergency:
                login(request, user)
                return redirect('Emergency')
            elif user is not None and user.is_Records :
                login(request, user)
                return redirect('Records')
            elif user is not None and user.is_Laboratory:
                login(request, user)
                return redirect('Laboratory')  
            elif user is not None and user. is_Pharmacy:
                login(request, user)
                return redirect('Pharmacy')   
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def admin(request):
    return render(request,'departments/admin.html')

@login_required
def opd(request):
    return render(request,'opd.html')

@login_required
def Theater(request):
    return render(request,'departments/theater.html')

@login_required
def Maternity(request):
    return render(request,'departments/maternity.html')

@login_required
def MFP(request):
    return render(request,'departments/MFP.html')

@login_required
def Emergency (request):
    return render(request,'departments/Emergency.html')

@login_required
def Records(request):
    return render(request,'departments/Records.html')

@login_required
def Pharmacy(request):
    return render(request,'departments/Pharmacy.html')

@login_required
def Laboratory(request):
    return render(request,'departments/Laboratory.html')

@login_required
def AC(request):
    return render(request,'departments/AC.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login_view')


def add_vitals(request):
    form = Patients_vitals_forms()
    if request.method == 'POST':
        form = Patients_vitals_forms(request.POST)
        if form.is_valid():
            form.save()
            form = Patients_vitals_forms()
    return render(request,'add_vitals.html',{'form': form,})

def patients_history(request):
    history = Patients_vitals.objects.all()
    return render(request,'patients_history.html',{'history': history})

def add_lab_results(request):
    form = Lab_results_forms()
    if request.method == 'POST':
        form = Lab_results_forms(request.POST)
        if form.is_valid():
            form.save()
            form = Lab_results_forms()
            messages.success(request, "Results added successfully")
    return render(request,'add_lab_results.html',{'form':form})

def AC_vitals_records(request):
    obj = AddRecord.objects.all()
    form = AC_vitals_forms()
    if request.method == 'POST':
        form = AC_vitals_forms(request.POST)
        if form.is_valid():
            form.save()
            form = AC_vitals_forms()
            messages.success(request, "Results added successfully")
    return render(request,'a&c_vitals_records.html',{'form':form, 'obj':obj})


def general_notes(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            form = NotesForm()
            messages.success(request, "Results added successfully")
    return render(request,'general_notes.html',{'form':form})

def theater_records(request):
    form = theater_Record()
    if request.method == 'POST':
        form = theater_Record(request.POST)
        if form.is_valid():
            form.save()
            form = theater_Record()
            messages.success(request, "Results added successfully")
    return render(request,'general_notes.html',{'form':form})

def maternity_notes_records(request):
    form = maternity_Record()
    if request.method == 'POST':
        form = maternity_Record(request.POST)
        if form.is_valid():
            form.save()
            form = maternity_Record()
            messages.success(request, "Results added successfully")
    return render(request,'maternity_notes.html',{'form':form})

def emergency_notes_records(request):
    form = emergency_Record()
    if request.method == 'POST':
        form = emergency_Record(request.POST)
        if form.is_valid():
            form.save()
            form = emergency_Record()
            messages.success(request, "Results added successfully")
    return render(request,'emergency_notes.html',{'form':form})

def emergency_notes_records(request):
    form = emergency_Record()
    if request.method == 'POST':
        form = emergency_Record(request.POST)
        if form.is_valid():
            form.save()
            form = emergency_Record()
            messages.success(request, "Results added successfully")
    return render(request,'emergency_notes.html',{'form':form})


def mfp_records(request):
    form = MFP_Record()
    if request.method == 'POST':
        form = MFP_Record(request.POST)
        if form.is_valid():
            form.save()
            form = MFP_Record()
            messages.success(request, "Results added successfully")
    return render(request,'mfp_notes.html',{'form':form})


def department_list(request):
    return render(request,'department_list.html')





