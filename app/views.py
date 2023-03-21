from django.shortcuts import render,redirect
from .models import inquiry
from .forms import inquiryForm, RecordForm, contact_us_form,appointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AddRecord
from django.db.models import Q
from members.models import Patients_vitals,Laboratory_results, Antenatal_care,theater_notes,maternity_notes,emergency_notes,MFP_notes
# Create your views here.

def index(request):
    form = inquiryForm()
    if request.method == 'POST':
      form = inquiryForm(request.POST)
      if form.is_valid():
           form.save()
           form = inquiryForm()
           messages.info(request, 'We will get back to you soon')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def appointment(request):
    form = appointmentForm()
    if request.method == 'POST':
      form = appointmentForm(request.POST,request.FILES)
      if form.is_valid():
           form.save()
           form = appointmentForm()
           messages.info(request, 'Appointment sent successfully')
    return render(request, 'appointment.html',{'form':form})

@login_required
def add_record(request):
    form = RecordForm()
    if request.method == 'POST':
      form = RecordForm(request.POST)
      if form.is_valid():
           form.save()
           form = RecordForm()
           messages.info(request, 'Record added successfully')
           return redirect('record_list')
    else:
        form = RecordForm()
    return render(request,'add_record.html',{'form':form})


def update_record(request, pk):
     if request.user.is_authenticated:
        current_record = AddRecord.objects.get(pk=pk)
        form = RecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('record_list')
        return render(request, 'update_record.html', {'form':form})
     else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('record_list')

@login_required
def record_details(request, pk):
    all = AddRecord.objects.get(pk=pk)
    vitals = Patients_vitals.objects.all()
    lab_results = Laboratory_results.objects.all()
    AC= Antenatal_care.objects.all()
    Theaters = theater_notes.objects.all()
    maternity = maternity_notes.objects.all()
    emergency = emergency_notes.objects.all()
    mfpp = MFP_notes.objects.all()
    return render(request, 'record_details.html', {'all':all,'mfpp':mfpp, 'vitals':vitals,'lab_results':lab_results, 'AC':AC,'Theaters':Theaters,'maternity':maternity,'emergency':emergency})

def record_list(request):
    obj = AddRecord.objects.all()
    return render(request,'record_list.html', {'obj': obj})

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete = AddRecord.objects.get(pk=pk)
        delete.delete()
        messages.success(request, "Record Deleted Successfully...")
        return render(request, 'delete_record.html', {'delete':delete})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('record_list')
    

def search_record(request):
    if request.method=='POST':
        searched = request.POST['searched']
        venues = AddRecord.objects.filter(name__contains=searched)
        context ={
            'searched': searched,
            'venues':venues
        }
        return render(request,'search_record.html',context)
    else:
       return render(request,'search_record.html')


def contact_Us(request):
    form = contact_us_form()
    if request.method == 'POST':
        form = contact_us_form(request.POST)
        if form.is_valid():
            form.save()
            form = contact_us_form()
            messages.success(request, "Results added successfully")
    return render(request,'contact_us.html',{'form':form})














