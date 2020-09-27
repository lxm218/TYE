from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tye-home'),
    path('about/', views.about, name='tye-about'),
    path('team/', views.team, name='tye-team'),
    path('team/leader', views.leader, name='tye-leader'),
    path('team/instructor', views.instructor, name='tye-instructor'),
    path('class/', views.course, name='tye-class'),
    path('event/', views.event, name='tye-event'),
]