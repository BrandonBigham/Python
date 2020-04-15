from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('owners', views.createowner),
    path('success', views.success)
]
