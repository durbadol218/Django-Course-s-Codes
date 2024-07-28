from django.shortcuts import render,redirect
from .models import CarModel, CommentModel
from .forms import CommentForm
from django.views.generic import DetailView
# Create your views here.

class carDetailsView(DetailView):
    model = CarModel
    template_name = 'car_details.html'
    pk_url_kwarg = 'id'
    
    def post(self,request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, "This comment has been saved successfully")
        return redirect('car_details', id=self.kwargs['id'])
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhanre store korlam
        comments = post.comments.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

# def CarDetails(request,id):
    # data = CarModel.objects.get(pk=id)
    
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.data = data
    #         comment.save()
    #         messages.success(request, "This comment has been saved successfully")
    #         return redirect('car_details',id= id)
    # else:
    #     form = CommentForm()
    # return render(request, 'car_details.html', {'data': data,'comment_form':form})