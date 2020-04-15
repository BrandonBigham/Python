from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<str:number>', views.show),
    path('<str:number>/edit', views.edit),
    path('<str:number>/delete', views.destroy),
    path('delete/<number>', views.delete)
]