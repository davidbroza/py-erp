from django.urls import path

from .views import index

urlpatters = [
    path("/", index, name="index"),
]
