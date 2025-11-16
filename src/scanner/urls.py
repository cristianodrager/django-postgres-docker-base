from django.urls import path
from . import views

urlpatterns = [
    path('', views.scanner, name='scanner'),
    path('<cpf>', views.scanner_read, name='scanner-read'),
]