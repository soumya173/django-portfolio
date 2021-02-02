from django.shortcuts import render
from .models import posts
from django.views import generic
# from django.views.decorators.http import require_GET
# from django.http import HttpResponse

# class based views for posts
class blogposts(generic.ListView):
    queryset = posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogposts.html'
    paginate_by = 4

# class based view for each post
class singlepost(generic.DetailView):
    model = posts
    template_name = "singlepost.html"
