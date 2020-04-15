from django.urls import path
from . import views
urlpatterns=[
    path('', views.createbook),
    path('author', views.createauthor),
    path('add/book', views.addbook),
    path('add/author', views.addauthor),
    path('book/info/<int:id>', views.displaybook),
    path('author/info/<int:id>', views.displayauthor),
    path('book/add/<int:id>', views.connectauthor),
    path('author/add/<int:id>', views.connectbook)
]