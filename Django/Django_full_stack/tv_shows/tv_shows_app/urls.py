from django.urls import path
from . import views
urlpatterns=[
    path('shows', views.index),
    path('add/show', views.addshow),
    path('proccess/show', views.createshow),
    path('edit/show/<int:id>', views.editshow),
    path('show/info/<int:id>', views.showinfo),
    path('edit/show/<int:id>/proccess', views.editshowproccess),
    path('show/destroy/<int:id>', views.deleteshow),
    path('', views.direct)
]