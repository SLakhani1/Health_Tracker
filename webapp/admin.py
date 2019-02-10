from django.contrib import admin
from . models import Patient
from . models import Record

admin.site.register(Patient)
admin.site.register(Record)