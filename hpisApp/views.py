from django.shortcuts import render
from django.http import HttpResponseRedirect    #for the second function
# Create your views here.


def home(request):
  return render(request, 'hpisApp/home.html')

def patientReg(request):
  return render(request, 'hpisApp/patientReg.html')

def medHis(request):
  return render(request, 'hpisApp/medHis.html')

def doc(request):
  return render(request, 'hpisApp/doc.html')
