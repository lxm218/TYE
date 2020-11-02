from django.urls import path
from .views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    add_to_cart
  
)
from . import views

app_name = 'enroll'

urlpatterns = [
    path('stuent/', StudentListView.as_view(), name='tye-student'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/new/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('add-to-cart/<slug>/', add_to_cart, name= 'add-to-cart')
    
]