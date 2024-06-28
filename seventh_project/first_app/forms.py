from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # exclude = ['roll']
        fields = '__all__'
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll'
        }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'btn-primary','color':'black'}),
        # }
        widgets  = {
            'name' : forms.TextInput(attrs={'class': 'btn-primary'}),
            # 'roll' : forms.PasswordInput()
        }
        help_texts = {
            'name' : "Write your full name"
        }
        
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }