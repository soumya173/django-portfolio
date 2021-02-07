from django.shortcuts import get_object_or_404
from .models import posts
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
# from django.views.decorators.http import require_GET

# class based views for posts
class blogposts(generic.ListView):
    queryset = posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogposts.html'
    paginate_by = 4

# class based view for each post
class singlepost(generic.DetailView):
    model = posts
    template_name = "singlepost.html"

    def get_context_data(self, *args, **kwargs):
        context = super(singlepost, self).get_context_data()
        objs = get_object_or_404(posts, id=self.kwargs['pk'])
        context['total_likes'] = objs.total_likes()
        return context

def likepost(request, pk):
    post = get_object_or_404(posts, id=request.POST.get('like_post_btn'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('singlepost', args=[str(pk)]))
