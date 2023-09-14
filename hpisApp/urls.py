from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patientReg/', views.patientReg, name='patientReg'),
    path('medHis/', views.medHis, name='medHis'),
    path('doc/', views.doc, name='doc'),
]


