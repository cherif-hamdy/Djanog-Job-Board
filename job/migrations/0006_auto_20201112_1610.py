# Generated by Django 3.1.3 on 2020-11-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='media/jobs/'),
        ),
    ]