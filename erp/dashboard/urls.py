from django.urls import path

from .views import index, test, test2

urlpatterns = [
    path("", index, name="index"),
    path("test/", test, name="test"),
    path("test2/", test2, name="test2"),
]
