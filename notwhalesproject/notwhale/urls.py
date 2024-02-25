from django.urls import path
from . import views

urlpatterns = [
    path("", views.helloworld, name='helloworld'),
    path("one/", views.func_1, name='func_1'),
    path("two/", views.func_2, name='func_2'),
]
