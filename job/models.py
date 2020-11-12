from django.db import models


JOB_Type = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20,choices=JOB_Type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category" , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='jobs/')

    def __str__(self):
        return self.title
    
