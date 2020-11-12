from django.shortcuts import render
from django.http import HttpResponse
from .models import Job , Category

# Create your views here.
def job_list(request):
    jobs =  Job.objects.all() 
    context = {'jobs' : jobs}
    return render(request , 'job/index.html' , context)


def job_detail(request , id):
    job = Job.objects.get(id=id) 
    context = {'job' : job}
    return render(request , 'job/detail.html' , context)