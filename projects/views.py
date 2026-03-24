from django.shortcuts import render
from django.http import HttpResponse

def getProjectsPage(request):
    return render(request, 'projects.html')

def project(reques, pk):
    return render(request, 'project.html')
