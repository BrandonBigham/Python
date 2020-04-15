from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path("add/teacher", views.teacher),
    path('add/student', views.student)
]