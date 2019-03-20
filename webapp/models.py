from django.db import models
from django.utils import timezone
from django.conf import settings
#from django.contrib.auth.models import AbstractUser

#class User(AbstractUser):
#    is_patient = models.BooleanField()
#    is_hospital = models.BooleanField()
#
#    def __str__(self):
#        return self.username

class Patient(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)

    adhaarId = models.IntegerField(primary_key=True)  #Add length of adhaar no
    fname = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=70)
    
    def __str__(self):
        return str(self.adhaarId)

class Record(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    patient = models.ForeignKey('webapp.Patient', on_delete=models.CASCADE, related_name='records')
    created_date = models.DateTimeField(default = timezone.now)
    hospital_name = models.CharField(max_length=50)
    hospital_address = models.CharField(max_length=70)
    admission_date = models.DateTimeField()
    discharge_date = models.DateTimeField()
    disease = models.TextField()
    treatment = models.TextField()
    treated_by = models.CharField(max_length=50)    #Doctor's name
    payment = models.IntegerField()

    def __str__(self):
        return str(self.patient)