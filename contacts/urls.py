from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_contact, name="create_contact"),
    path("privacy/", views.privacy, name="privacy"),
]