from django.shortcuts import render
from django.http import HttpResponseRedirect   
from django.urls import reverse
from .models import PatientReg
from .models import MedHistory
from .forms import PatientRegForm
from .forms import MedHistoryForm



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





def deletePatient(request, id):
  if request.method == 'POST':
    patientReg = PatientReg.objects.get(pk=id)
    patientReg.delete()
  return HttpResponseRedirect(reverse('patientReg'))













# MEDICAL HISTORY
def medHis(request):
  return render(request, 'hpisApp2/medHis.html',
    {'medHis': MedHistory.objects.all()} 
  )



def view_medHis(request, id):
  medHis = MedHistory.objects.get(pk=id)
  return HttpResponseRedirect (reverse('medHis'))      #no need to hardcode index.html....use reverse para ma tawag tong other view nga index


def editmedHis(request, id):
  if request.method == 'POST':
    medHis= MedHistory.objects.get(pk=id)
    form = MedHistoryForm(request.POST, instance=medHis)
    if form.is_valid():
      form.save()
      return render(request, 'hpisApp2/editmedHis.html', {
        'form': form,
        'success': True
      })
  else:
    medHis = MedHistory.objects.get(pk=id)
    form = MedHistoryForm(instance=medHis)
  return render(request, 'hpisApp2/editmedHis.html', {
    'form': form
  })


def addmedHis(request):
  if request.method == 'POST':
    form = MedHistoryForm(request.POST)
    if form.is_valid():
      #gibutang another variable
      new_medhis_id = form.cleaned_data['medhis_id']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_doctor = form.cleaned_data['doctor']
      new_bp = form.cleaned_data['bp']
      new_diagnosis = form.cleaned_data['diagnosis']
      new_medication = form.cleaned_data['medication']


      #then gibalik napud on the same nam variable before
      #PatientReg comes from models
      new_medHis = MedHistory(   
        medhis_id=new_medhis_id,
        first_name=new_first_name,
        last_name=new_last_name,
        doctor=new_doctor,
        bp=new_bp,
        diagnosis=new_diagnosis,
        medication=new_medication
      )

      new_medHis.save()
      return render(request, 'hpisApp2/addmedHis.html', {
        'form': MedHistoryForm(),
        #if saved, naay notif for confirmation nga na success ang process of adding list
        'success': True
      })
  else:
    form = MedHistoryForm()
  return render(request, 'hpisApp2/addmedHis.html', {
    'form': MedHistoryForm()
  })





def deletemedHis(request, id):
  if request.method == 'POST':
    medHis = MedHistory.objects.get(pk=id)
    medHis.delete()
  return HttpResponseRedirect(reverse('medHis'))



# def medHis(request):
#   return render(request, 'hpisApp2/medHis.html')

def doc(request):
  return render(request, 'hpisApp/doc.html')
