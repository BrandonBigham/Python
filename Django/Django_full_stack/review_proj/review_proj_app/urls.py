from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('users', views.createUser),
    path('login', views.login),
    path('homepage', views.homepage),
    path('cats', views.createCat),
    path('delete/<int:id>', views.deletecat),
    path('vote/<int:id>', views.votecat),
    path('unvote/<int:id>', views.unvotecat),
    path('profile', views.userprofile),
    path('cat/<int:id>', views.catprofile)
]