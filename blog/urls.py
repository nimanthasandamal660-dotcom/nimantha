from django.urls import path
from .views import (
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    about,
    contact,
    home,
)

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<slug:slug>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]