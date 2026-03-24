from django.shortcuts import render
from django.http import HttpResponse

def getProjectsPage(request):
    return HttpResponse('This our Projects Page')

def project(reques, pk):
    return HttpResponse('This is project page' + ' ' + str(pk))
