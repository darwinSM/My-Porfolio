from django.urls import path
from app_projects import views

urlpatterns = [
    path('projects/', views.projects_view, name='projects_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
]