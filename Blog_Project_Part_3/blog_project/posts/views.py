from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST': # user post request koreche
        post_form = forms.PostForm(request.POST) #user kisu akta data pathaise,form ta ar khali nai!
        if post_form.is_valid(): # post kora data gula valid kina seta check kortechi
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save() # data valid hoile seta database a save korbo!
            return redirect('add_post') # sobkisu thik thaakle taake ai 'url' a paathaay dibo directly!
    else: # user normally website a gele blank form paabe!
        post_form = forms.PostForm()
    return render(request, 'add_post.html',{'form':post_form})


# Add post using class Based View
@method_decorator(login_required,name='dispatch') # non-logged in user access korte paarbe na kokhono!
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('homepage') # return render er poriborte amra "reverse_lazy" use kori!
    
    #form validate korar jonno ai kaaj korte hobe!
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    # print(post.title)
    if request.method == 'POST': # user post request koreche
        post_form = forms.PostForm(request.POST,instance=post) #user kisu akta data pathaise,form ta ar khali nai!
        if post_form.is_valid(): # post kora data gula valid kina seta check kortechi
            post_form.instance.author = request.user
            post_form.save() # data valid hoile seta database a save korbo!
            return redirect('homepage') # sobkisu thik thaakle taake ai 'url' a paathaay dibo directly!
    return render(request, 'add_post.html',{'form':post_form})


# Add post using class Based View
@method_decorator(login_required,name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('authorProfile') # return render er poriborte amra "reverse_lazy" use kori!
    pk_url_kwarg = 'id'
    
    #form validate korar jonno ai kaaj korte hobe!
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage') # sobkisu thik thaakle taake ai 'url' a paathaay dibo directly!


# Add post using class Based View
@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    # form_class = forms.PostForm    #delete korar jonno form dorkar hoy na!
    template_name = 'delete_post.html'
    success_url = reverse_lazy('authorProfile') # return render er poriborte amra "reverse_lazy" use kori!
    pk_url_kwarg = 'id'
    
    
class DetailsPostView(DetailView):
    model = models.Post
    template_name = 'post_details.html'
    pk_url_kwarg = 'id'
    
    def post(self,request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(self,request, *args, **kwargs)
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhanre store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        # if self.request.method == 'POST':
        #     comment_form = forms.CommentForm(data=self.request.POST)
        #     if comment_form.is_valid():
        #         new_comment = comment_form.save(commit=False)
        #         new_comment.post = post
        #         new_comment.save()
        #         return redirect('post_details')
        # else:
        #     comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context