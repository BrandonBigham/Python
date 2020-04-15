from django.urls import path
from . import views
urlpatterns=[
    path('', views.index),
    path('process/gold', views.process),
    path('<path:route>', views.wrong)
]