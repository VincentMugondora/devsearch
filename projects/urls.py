from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.getProjectsPage),
    path('project/<str:pk>/', views.project),
]
