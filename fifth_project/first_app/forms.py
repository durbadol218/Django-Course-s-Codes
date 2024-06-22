from django import forms
from django.core import validators
# widgets == field to html input

class contactForm(forms.Form):
    name = forms.CharField(label="Full Name: ",help_text="Total length must be within 70 characters",required=True,widget=forms.Textarea(attrs = {'id': 'text_area','class':'class1','placeholder':'Enter your name'}))
    # file = forms.FileField()
    email = forms.EmailField(label="User Email")
    # age = forms.IntegerField(label="Age")
    # weight = forms.FloatField()
    # balance = forms.DecimalField(label="Balance")
    
    age = forms.CharField(widget=forms.NumberInput())
    check = forms.BooleanField(label="Check")
    birthday = forms.CharField(label="Birthday",widget=forms.DateInput(attrs={'type':'date'}))
    appoinment = forms.DateTimeField(label="Appoinment",widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICE = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICE, widget=forms.RadioSelect())
    MEAL =[('P','Pepperoni'),('M','Mashroom'),('C','Chicken')]
    pizza = forms.MultipleChoiceField(choices = MEAL,widget=forms.CheckboxSelectMultiple)
    
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget = forms.TextInput)
#     email = forms.CharField(widget = forms.EmailInput)
    
#     # MAnual Validators!
    
#     # def clean_name(self):
#     #     valName = self.cleaned_data['name']
#     #     if len(valName) < 10:
#     #         raise forms.ValidationError("Enter a name with atleast 10 characters!")
#     #     return valName
#     # def clean_email(self):
#     #     valEmail = self.cleaned_data['email']
#     #     if '.com' not in valEmail:
#     #         raise forms.ValidationError("Your email must contain .com")
#     #     return valEmail
    
#     def clean(self):
#         clean_data = super().clean()
#         valName = self.cleaned_data['name']
#         valEmail = self.cleaned_data['email']
#         if len(valName) < 10:
#             raise forms.ValidationError("Enter a name with atleast 10 characters!")
#         valEmail = self.cleaned_data['email']
#         if '.com' not in valEmail:
#             raise forms.ValidationError("Your email must contain .com")




class StudentData(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10,message='Enter a name with maximum 10 characters!')])
    name = forms.CharField(validators=[validators.MinLengthValidator(10,message='Enter a name with atleast 10 characters!')])
    email = forms.CharField(widget = forms.EmailInput,validators=[validators.EmailValidator(message='Enter a valid email address')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(35),validators.MinValueValidator(10)])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'])])
    
    
    
class PasswordValidatioProject(forms.Form):
    name = forms.CharField(widget = forms.TextInput)
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    
    
    def clean(self):
        cleaned_data = super().clean()
        valPass = self.cleaned_data['password']
        valConfirm = self.cleaned_data['confirm_password']
        valName = self.cleaned_data['name']
        if valPass != valConfirm:
            raise forms.ValidationError("Password does not match!")
        if len(valName) < 15:
            raise forms.ValidationError("Name must be at least 15 characters!")