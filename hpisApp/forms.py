#used for forms if need nag input data from users, adding data

from django import forms
from .models import PatientReg

class PatientRegForm(forms.ModelForm):
    class Meta:
        model = PatientReg
        #fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        #since we are selecting all model fields nga ato inputan, we use __all__
        fields = '__all__'

        #labels is used as label since we dont want to use default model fields (ex. last____name)
        labels = {
            'patient_id': 'Patient ID', 
            'first_name': 'First Name', 
            'last_name': 'Last Name',
            'sex': 'Sex', 
            'address': 'Address',
        }

        #widgets handles the rendering and extraction of data from get or post dictionary that corresponds to the widgets
        widgets = {
            'patient_id': forms.NumberInput(attrs={'class': 'form-control'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }