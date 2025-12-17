from django.urls import path
from . import views

urlpatterns = [
    path("", views.turmas, name="turmas"),  # Placeholder view
    path("turma/<int:id>/", views.turma, name="turma"),  # Placeholder view
    path("filter/", views.turmas_filter, name="turmas-filter"),  # Placeholder view
    path(
        "filter/search/<student_id>",
        views.turmas_filter_search,
        name="turmas-filter-search",
    ),
    path(
        "add-student-turma/<int:turma_id>/<int:student_id>/",
        views.add_student_turma,
        name="add-student-turma",
    ),
    path(
        "remove-student-turma/<int:turma_id>/<int:student_id>/",
        views.remove_student_turma,
        name="remove-student-turma",
    ),
]
