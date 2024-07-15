from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def add_category(request):
    if request.method == 'POST': # user post request koreche
        category_form = forms.CategoryForm(request.POST) #user kisu akta data pathaise,form ta ar khali nai!
        if category_form.is_valid(): # post kora data gula valid kina seta check kortechi
            category_form.save() # data valid hoile seta database a save korbo!
            return redirect('add_category') # sobkisu thik thaakle taake ai 'url' a paathaay dibo directly!
    else: # user normally website a gele blank form paabe!
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html',{'form':category_form})