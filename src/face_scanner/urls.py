from django.urls import path
from . import views

urlpatterns = [
    path("", views.face_scanner, name="face-scanner"),
    path("register-face/", views.register_face, name="register-face"),
    path("face-login/", views.face_login, name="face-login"),
    path("face-recognition/", views.face_recognition, name="face-recognition"),
    # path("format", views.format_descriptor, name="face-format"),
]
