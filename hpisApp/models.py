from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class PatientReg(models.Model):
    patient_id= models.CharField(max_length=50)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    sex= models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    #contact_number = PhoneNumberField()


    #code para ma show sa admin database and ma control
    def __str__(self):
      return f'Patient {self.first_name} {self.last_name}'

