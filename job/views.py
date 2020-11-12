from django.shortcuts import render
from django.http import HttpResponse
from .models import Job , Category

# Create your views here.
def job_list(request):
    jobs =  Job.objects.all()
    return HttpResponse(jobs)


def job_detail(request , id):
    return HttpResponse("hello world") 