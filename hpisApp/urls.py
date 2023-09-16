from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('patientReg/', views.patientReg, name='patientReg'),
    path('<int:id>', views.view_patientReg, name='view_patientReg'),   #to call specific patientReg
    path('patientReg/addPatient/', views.addPatient, name='addPatient'),
    path('patientReg/editPatient/<int:id>/', views.editPatient, name='editPatient'),
    path('medHis/', views.medHis, name='medHis'),
    path('doc/', views.doc, name='doc'),

]


