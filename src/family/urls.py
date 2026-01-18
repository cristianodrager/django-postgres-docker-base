from django.urls import path
from . import views

urlpatterns = [
    path("pk/<cpf>", views.family, name="family"),
    path("family-face", views.family_face, name="family-face"),
    path("add-family", views.add_family_form, name="add-family"),
    path("edit-family", views.edit_family_form, name="edit-family"),
    path("add-family-save", views.add_family_save, name="add-family-save"),
    path("search-family/<pk>", views.search_family, name="search-family"),
]
