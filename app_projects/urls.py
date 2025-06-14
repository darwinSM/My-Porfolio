from django.urls import path
from app_projects import views

urlpatterns = [
    path('projects/', views.projects_view, name='projects_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    #Temporales
    path('temporal-load-fixtures/', views.temporal_load_fixtures_view, name="temporal_load_fixtures"),
    path('test-upload/', views.test_cloudinary_upload, name='test_cloudinary_upload'),
]