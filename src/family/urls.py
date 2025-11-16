from django.urls import path
from . import views

urlpatterns = [
    path('<cpf>', views.family, name='family'),
]