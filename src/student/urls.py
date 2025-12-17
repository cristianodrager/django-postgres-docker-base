from django.urls import path
from . import views

urlpatterns = [
    path("pk/<id>", views.student, name="student"),
    path("search", views.search, name="search-student"),
    path("search-results", views.search_results, name="search-results"),  # htmx
    path(
        "add-legal-resp/<student_id>/<legal_resp_id>",
        views.add_legal_resp,
        name="add-legal-resp",
    ),
    path(
        "remove-legal-resp/<legal_resp_student_id>",
        views.remove_legal_resp,
        name="remove-legal-resp",
    ),
]
