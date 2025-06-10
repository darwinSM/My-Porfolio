from django.urls import path
from app_about_me import views

urlpatterns = [
    path("", views.about_me_view, name="about_me"),
]