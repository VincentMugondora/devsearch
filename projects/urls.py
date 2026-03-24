from django.urls import path
from . import views

urlpatterns = [
    path('', views.getProjectsPage),
    path('project/<str:pk>/', views.project),
]
