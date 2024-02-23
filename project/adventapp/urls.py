from django.urls import path
from . import views

urlpatterns = [
    path("slots", views.get_slot)
]