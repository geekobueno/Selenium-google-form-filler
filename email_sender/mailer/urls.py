from django.urls import path
from .views import send_assignment_email

urlpatterns = [
    path('send-email/', send_assignment_email, name='send_email'),
]
