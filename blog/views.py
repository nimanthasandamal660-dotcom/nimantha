from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Category, Post


# Post List View (Class-Based View)
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status="published").order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Sidebar එකට අවශ්‍ය Categories සියල්ල ලබා ගැනීම
        context["categories"] = Category.objects.all()
        return context


# Post Detail View (Class-Based View)
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(status="published")


# Static Pages (Function-Based Views)
def home(request):
    return render(request, "blog/home.html")


def about(request):
    return render(request, "blog/about.html", {"team": "DjangoBlog Team"})


def contact(request):
    return render(request, "blog/contact.html")