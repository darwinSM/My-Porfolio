from django.urls import path
from app_contact import views
from app_contact.views import ContactMessageListView, ContactMessageDetailView, ContactMessageUpdateView, ContactMessageDeleteView

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('contact-messages-list', ContactMessageListView.as_view(), name="contact_messages_list"),
    path('contact-message-detail/<int:pk>/', ContactMessageDetailView.as_view(), name="contact_message_detail"),
    path('contact-message-update/<int:pk>/', ContactMessageUpdateView.as_view(), name="contact_message_update"),
    path('contact-message-delete/<int:pk>/', ContactMessageDeleteView.as_view(), name="contact_message_delete"),
]