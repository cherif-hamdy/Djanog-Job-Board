# Generated by Django 3.1.3 on 2020-11-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]