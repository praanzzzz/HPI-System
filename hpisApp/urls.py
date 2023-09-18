from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('patientReg/', views.patientReg, name='patientReg'),
    path('<int:id>', views.view_patientReg, name='view_patientReg'),   #to call specific patientReg
    path('patientReg/addPatient/', views.addPatient, name='addPatient'),
    path('patientReg/editPatient/<int:id>/', views.editPatient, name='editPatient'),
    path('deletePatient/<int:id>/', views.deletePatient, name='deletePatient'),


    path('medHis/', views.medHis, name='medHis'),
    path('<int:id>', views.view_medHis, name='view_medHis'),   #to call specific patientReg
    path('medHis/addmedHis/', views.addmedHis, name='addmedHis'),
    path('medHis/editmedHis/<int:id>/', views.editmedHis, name='editmedHis'),
    path('deletemedHis/<int:id>/', views.deletemedHis, name='deletemedHis'),

    
    path('doc/', views.doc, name='doc'),

]


