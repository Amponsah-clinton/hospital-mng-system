from django.db import models
from django.contrib.auth.models import AbstractUser
from app.models import AddRecord

# Create your models here.

class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_OPD = models.BooleanField('Is OPD', default=False)
    is_A_and_C = models.BooleanField('Is A&C', default=False)
    is_Theater = models.BooleanField('Is Theater', default=False)
    is_Maternity = models.BooleanField('Is Maternity', default=False)
    is_Male = models.BooleanField('Is Male,Female&Pedeatics', default=False)
    is_Emergency = models.BooleanField('Is Emergency', default=False)
    is_Records = models.BooleanField('Is Records', default=False)
    is_Pharmacy = models.BooleanField('Is Pharmacy', default=False)
    is_Laboratory = models.BooleanField('Is Laboratory', default=False)
  
class Patients_vitals(models.Model):
    pulse = models.IntegerField()
    weight = models.IntegerField()
    pressure = models.IntegerField()
    patient = models.ForeignKey(AddRecord, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
   
    def __str__(self):
        return self.patient.name 
    
class Laboratory_results(models.Model):
    patient = models.ForeignKey(AddRecord, on_delete=models.CASCADE)
    Results = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.patient.name + ' || ' + self.patient.Folder_number

class Antenatal_care(models.Model):
    patient = models.ForeignKey(AddRecord, on_delete=models.CASCADE)
    body_examination = models.TextField()
    drugs = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.patient.name + ' || ' + self.patient.Folder_number    


class Notes(models.Model):
     patient = models.ForeignKey(AddRecord, on_delete=models.CASCADE)
     Findings = models.TextField()
     Drug_Prescriptions = models.TextField()


     def __str__(self):
        return self.patient.name + ' || ' + self.patient.Folder_number    
 
class theater_notes(models.Model):
    patient = models.ForeignKey(AddRecord, on_delete=models.CASCADE)
    body_examination = models.TextField()
    drugs = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.patient.name + ' || ' + self.patient.Folder_number    


class maternity_notes(models.Model):
    patient = models.ForeignKey(AddRecord, on_delete=models.CASCADE)
    body_examination = models.TextField()
    drugs = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.patient.name + ' || ' + self.patient.Folder_number    


class emergency_notes(models.Model):
    patient = models.ForeignKey(AddRecord, on_delete=models.CASCADE)
    body_examination = models.TextField()
    drugs = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.patient.name + ' || ' + self.patient.Folder_number    

class MFP_notes(models.Model):
    patient = models.ForeignKey(AddRecord, on_delete=models.CASCADE)
    body_examination = models.TextField()
    drugs = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.patient.name + ' || ' + self.patient.Folder_number    