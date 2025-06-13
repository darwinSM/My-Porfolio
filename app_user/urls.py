from django.urls import path
from app_user import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/" , views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("create-superuser-render/", views.temporal_create_superuser_render_view),
]