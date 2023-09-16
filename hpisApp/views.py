from django.shortcuts import render
from django.http import HttpResponseRedirect   
from django.urls import reverse
from .models import PatientReg
from .forms import PatientRegForm



def dashboard(request):
  return render(request, 'hpisApp/dashboard.html')

def patientReg(request):
  return render(request, 'hpisApp/patientReg.html',
    {'patientReg': PatientReg.objects.all()}  #referring to models (PatientReg) , patientReg is the new variable ani
  )


#get me the specific patient Registration that whose primary key is equal to the database passed to the argument
def view_patientReg(request, id):
  patientReg = PatientReg.objects.get(pk=id)
  return HttpResponseRedirect (reverse('patientReg'))      #no need to hardcode index.html....use reverse para ma tawag tong other view nga index


def editPatient(request, id):
  if request.method == 'POST':
    patientReg= PatientReg.objects.get(pk=id)
    form = PatientRegForm(request.POST, instance=patientReg)
    if form.is_valid():
      form.save()
      return render(request, 'hpisApp/editPatient.html', {
        'form': form,
        'success': True
      })
  else:
    patientReg = PatientReg.objects.get(pk=id)
    form = PatientRegForm(instance=patientReg)
  return render(request, 'hpisApp/editPatient.html', {
    'form': form
  })


def addPatient(request):
  if request.method == 'POST':
    form = PatientRegForm(request.POST)
    if form.is_valid():
      #gibutang another variable
      new_patient_id = form.cleaned_data['patient_id']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_sex = form.cleaned_data['sex']
      new_address = form.cleaned_data['address']


      #then gibalik napud on the same nam variable before
      #PatientReg comes from models
      new_patientReg = PatientReg(   
        patient_id=new_patient_id,
        first_name=new_first_name,
        last_name=new_last_name,
        sex=new_sex,
        address=new_address,
      )

      new_patientReg.save()
      return render(request, 'hpisApp/addPatient.html', {
        'form': PatientRegForm(),
        #if saved, naay notif for confirmation nga na success ang process of adding list
        'success': True
      })
  else:
    form = PatientRegForm()
  return render(request, 'hpisApp/addPatient.html', {
    'form': PatientRegForm()
  })







def medHis(request):
  return render(request, 'hpisApp/medHis.html')

def doc(request):
  return render(request, 'hpisApp/doc.html')
