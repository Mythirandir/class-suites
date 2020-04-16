from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("rooms/", views.rooms, name="rooms"),
    path("contact/", views.contact, name="contact"),
]
