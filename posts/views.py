from django.views.generic import ListView

from .models import Post


class HomePageView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'


