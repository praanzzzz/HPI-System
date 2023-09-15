from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('patientReg/', views.patientReg, name='patientReg'),
    path('medHis/', views.medHis, name='medHis'),
    path('doc/', views.doc, name='doc'),
]


