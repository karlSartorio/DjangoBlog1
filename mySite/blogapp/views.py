from django.shortcuts import render
from blogapp.models import Post, Comment
from blogapp.forms import PostForm, CommentForm
form django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin # login required but Class based views.

from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)

# Create your views here.

class AboutUsView(TemplateView):
    #DESCRIPTION
    #creating views for the about us page.
    temaplate_name = 'aboutus.html'

class PostListView(ListView):
    #DESCRIPTION:
    #this is the home page view,
    model = Post

    def get_queryset(self):
    #DESCRIPTION
    # this class method will define the list - how its going to get info from
    # model the. this allows django's ORM or allows to use SQL query into the model
    return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    ## NOTE:
    # something to note about this code: this code gets all the object in the model, filters them using the published_date.
    # next to continue on, '__' you can set the field conditions. for this instance its 'lte' - less than or equal to.
    # so to continue, its less than or equal to the timezone now, ordered by published_date. the '-' means DESC in SQL
    # meaning the newest first. its defaulted at oldest first. This will continue on through out the views

class PostDetailView(DetailView):
    #DESCRIPTION:
    # create a view that allows the user to click in the list of blog post to
    # its details. each post has a primary key to link to it.

    model = Post

################################################################################
#                               C*UD(CRUD) - Post View.                              #
################################################################################

# the method that uses Login required with Class based views

class PostCreateView(LoginRequiredMixin, CreateView):
    #DESCRIPTION:
    # this class view gives an allows LOGGED IN user to create a new post
    # and connect to the models

    login_url = '/login'# if a user want to create a post and not logged in, it will redirect them to the login page
    redirect_field_name = 'blogapp/post_detail.html' # redirect them to detail view if logged in

    form_class = PostForm # connect the form.py to show input the forms we defined.
    model = Post #DB connection

class PostUpateView(LoginRequiredMixin, UpdateView):
    #DESCRIPTION:
    # The same as the Create view, as you are simply recreating the same post.

    login_url = '/login'# if a user want to create a post and not logged in, it will redirect them to the login page
    redirect_field_name = 'blogapp/post_detail.html' # redirect them to detail view if logged in

    form_class = PostForm # connect the form.py to show input the forms we defined.
    model = Post #DB connection

class PostDeleteView(LoginRequiredMixin, DeleteView):
    #DESCRIPTION:
    # the user has to be loged in to see this view.
    # it is connected to the model, however, when using the delete view
    # you need to have a success redirect url

    model = Post
    success_url = reverse_lazy('post_list') # once the user deletes the blogm send back to the list of blogs
####################################END OF POST C*UD#####################################

class DraftListView(LoginRequiredMixin, ListView):
    #DESCRIPTION:
    # When a user is creating a post, they can create a draft. this is the view
    # that allows this to happen.


    login_url = '/login' # redirect to login page if not logged in
    redirect_field_name = 'blog/post_list.html' # direct to post list.

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True)).order_by('created_date')
