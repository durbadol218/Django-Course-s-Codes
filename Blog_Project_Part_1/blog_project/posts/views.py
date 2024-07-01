from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_post(request):
    if request.method == 'POST': # user post request koreche
        post_form = forms.PostForm(request.POST) #user kisu akta data pathaise,form ta ar khali nai!
        if post_form.is_valid(): # post kora data gula valid kina seta check kortechi
            post_form.save() # data valid hoile seta database a save korbo!
            return redirect('add_post') # sobkisu thik thaakle taake ai 'url' a paathaay dibo directly!
    else: # user normally website a gele blank form paabe!
        post_form = forms.PostForm()
    return render(request, 'add_post.html',{'form':post_form})



def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    # print(post.title)
    if request.method == 'POST': # user post request koreche
        post_form = forms.PostForm(request.POST,instance=post) #user kisu akta data pathaise,form ta ar khali nai!
        if post_form.is_valid(): # post kora data gula valid kina seta check kortechi
            post_form.save() # data valid hoile seta database a save korbo!
            return redirect('homepage') # sobkisu thik thaakle taake ai 'url' a paathaay dibo directly!
    return render(request, 'add_post.html',{'form':post_form})



def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage') # sobkisu thik thaakle taake ai 'url' a paathaay dibo directly!