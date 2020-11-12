from django.urls import path
from . import views

urlpatterns = [
    path("" , views.job_list , name='jobs'),
    path("<int:id>/" , views.job_detail , name="job_detail"),
]