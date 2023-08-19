from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name="global_index"),
    path("", views.get_started, name="get_started")
]