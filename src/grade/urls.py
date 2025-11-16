from django.urls import path
from . import views

urlpatterns = [
    path('', views.turmas , name='turmas'),  # Placeholder view
    path('turma/<int:id>/', views.turma , name='turma'),  # Placeholder view
]