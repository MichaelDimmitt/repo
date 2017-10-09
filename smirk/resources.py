from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from smirk.models import *

from django.db import models
from django.contrib.auth.models import User

# Create your API endPoints here.

#System Administrator Role
class System_Administrator(ModelResource):
    class Meta:
	queryset = System_Administrator.objects.all()
	resource_name = 'System_Administrator'
	authorization = Authorization()

#Doctor Role
class Doctor(ModelResource):
    class Meta:
	queryset = Doctor.objects.all()
	resource_name = 'Doctor'
	authorization = Authorization()

#Nurse Role
class Nurse(ModelResource):
    class Meta:
	queryset = Nurse.objects.all()
	resource_name = 'Nurse'
	authorization = Authorization()

#Medical Administrator Role
class Medical_Administrator(ModelResource):
    class Meta:
	queryset = Medical_Administrator.objects.all()
	resource_name = 'Medical_Administrator'
	authorization = Authorization()

#Insurance Administrator Role
class Insurance_Administrator(ModelResource):
    class Meta:
	queryset = Insurance_Administrator.objects.all()
	resource_name = 'Insurance_Administrator'
	authorization = Authorization()

#Patient Role
class Patient(ModelResource):
    class Meta:
	queryset = Patient.objects.all()
	resource_name = 'Patient'
	authorization = Authorization()

#Record
class Record(ModelResource):
    class Meta:
	queryset = Record.objects.all()
	resource_name = 'Record'
	authorization = Authorization()

#Doctor Exam Record
class Doctor_Exam_Record(ModelResource):
    class Meta:
	queryset = Doctor_Exam_Record.objects.all()
	resource_name = 'Doctor_Exam_Record'
	authorization = Authorization()

#Diagnosis Record
class Diagnosis_Record(ModelResource):
    class Meta:
	queryset = Diagnosis_Record.objects.all()
	resource_name = 'Diagnosis_Record'
	authorization = Authorization()

#Test Results Record
class Test_Results_Record(ModelResource):
   class Meta:
	queryset = Test_Results_Record.objects.all()
	resource_name = 'Test_Results_Record'
	authorization = Authorization()


#Insurance Claim Record
class Insurance_Claim_Record(ModelResource):
   class Meta:
	queryset = Insurance_Claim_Record.objects.all()
	resource_name = 'Insurance_Claim_Record'
	authorization = Authorization()


#Patient_Doctor_Correspondence_Record
class Patient_Doctor_Correspondence_Record(ModelResource):
    class Meta:
	queryset = Patient_Doctor_Correspondence_Record.objects.all()
	resource_name = 'Patient_Doctor_Correspondence_Record'
	authorization = Authorization()

#Raw Record
class Raw_Record(ModelResource):
    class Meta:
	queryset = Raw_Record.objects.all()
	resource_name = 'Raw_Record'
	authorization = Authorization()

#Note
class Note(ModelResource):
    class Meta:
	queryset = Note.objects.all()
	resource_name = 'Note'
	authorization = Authorization()

