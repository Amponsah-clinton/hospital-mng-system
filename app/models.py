from django.db import models
# Create your models here.

class inquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=2000)
    def __str__(self):
        return self.name + ' || ' + self.email
    
class AddRecord(models.Model):
        GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)
        name = models.CharField(max_length=400)
        age = models.IntegerField()
        gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
        House_number = models.CharField(max_length=100)
        Residence = models.CharField(max_length=200)
        Next_of_Kin = models.CharField(max_length=200)
        Phone_number = models.CharField(max_length=200)
        Occupation = models.CharField(max_length=200)
        NHIS_number = models.CharField(max_length=50)
        date = models.DateTimeField(auto_now_add=True)
        Folder_number = models.CharField(max_length=30)

        def __str__(self):
             return self.name + " " + self.NHIS_number


class contact_us(models.Model):
     name = models.CharField(max_length=200)
     email = models.EmailField(max_length=200)
     message = models.TextField(max_length=4100)

     def __str__(self):
            return self.name + " |||| " + self.email

class Doctor(models.Model):
        name = models.CharField(max_length=200)
        email = models.EmailField(max_length=200)
        hospital_number = models.CharField(max_length=200)
        date = models.DateTimeField(auto_now_add=True)
        def __str__(self):
              return self.name + " |||| " + self.hospital_number



class appointment(models.Model):
      name = models.CharField(max_length=200)
      email = models.EmailField(max_length=200)
      phone_number = models.CharField(max_length=11)
      complains = models.TextField(max_length=300)
      date = models.DateTimeField()
      NHIS = models.ImageField(null=True, blank=True, upload_to="images/")
      Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
      def __str__(self):
              return self.name + " |||| " + self.phone_number+ " |||| " + self.Doctor.name






