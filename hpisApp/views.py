from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect   
from django.urls import reverse
from .models import PatientReg
from .models import MedHistory
from .forms import PatientRegForm
from .forms import MedHistoryForm
#auth imports here
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required





def register(request):
    #fetch data from registration form
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
      #save to database
        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        return redirect('Login')
    return render(request, 'auth/register.html', {})

# capital L since naay function nga login which cannot be used to naming
def Login(request):
    if request.method == 'POST':
        #fetch data from login form
        name = request.POST.get('uname')
        password = request.POST.get('pass')
    #authenticate
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse('Error, user does not exist')
       
    return render(request, 'auth/Login.html', {})


@login_required
def logoutuser(request):
    logout(request)
    return redirect('Login')

@login_required
def dashboard(request):
  return render(request, 'hpisApp/dashboard.html')

@login_required
def patientReg(request):
  return render(request, 'hpisApp/patientReg.html',
    {'patientReg': PatientReg.objects.all()}  #referring to models (PatientReg) , patientReg is the new variable ani
  )

@login_required
#get me the specific patient Registration that whose primary key is equal to the database passed to the argument
def view_patientReg(request, id):
  patientReg = PatientReg.objects.get(pk=id)
  return HttpResponseRedirect (reverse('patientReg'))      #no need to hardcode index.html....use reverse para ma tawag tong other view nga index

@login_required
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

@login_required
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




@login_required
def deletePatient(request, id):
  if request.method == 'POST':
    patientReg = PatientReg.objects.get(pk=id)
    patientReg.delete()
  return HttpResponseRedirect(reverse('patientReg'))












@login_required
# MEDICAL HISTORY
def medHis(request):
  return render(request, 'hpisApp2/medHis.html',
    {'medHis': MedHistory.objects.all()} 
  )


@login_required
def view_medHis(request, id):
  medHis = MedHistory.objects.get(pk=id)
  return HttpResponseRedirect (reverse('medHis'))      #no need to hardcode index.html....use reverse para ma tawag tong other view nga index

@login_required
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

@login_required
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


@login_required
def deletemedHis(request, id):
  if request.method == 'POST':
    medHis = MedHistory.objects.get(pk=id)
    medHis.delete()
  return HttpResponseRedirect(reverse('medHis'))



@login_required
def doc(request):
  return render(request, 'hpisApp/doc.html')
