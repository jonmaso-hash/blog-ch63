
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
)
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.
class PostListView(ListView):  # GET Request -> List
    # Template_name attribute renders a specific html file
    template_name = "posts/list.html"
    
    # model attribute lets Django know from which model (Table) we want to retrieve the data
    model = Post
    
    # context_object_name attribute is used to change the variable name inside the template
    context_object_name = "posts"

class PostDetailView(DetailView): #GET Request -> Object
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView): #Post request -> form (HTML)
    template_name = "posts/new.html"
    model = Post
    #fields attribute is a list that allow us to enable/disable the inputs to render in the html
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = User.objects.last()
        print(form.instance)
        print(form)
        return super().form_valid(form)

class PostUpdateView(UpdateView): #POST Request -> filled form (HTML)
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView): #POST Request 
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")
