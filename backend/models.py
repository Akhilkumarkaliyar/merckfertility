from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Updates(models.Model):
    title_EN = models.CharField(max_length=255, null=False)
    title_AR = models.CharField(max_length=255, null=False)
    description_EN = RichTextField(max_length=255, null=False)
    description_AR = RichTextField(max_length=255, null=False)
    image = models.ImageField(upload_to='media/image',default='')
    is_delete=models.SmallIntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'f_update'

class Hospital(models.Model):
    title_EN= models.CharField(max_length=255, null=False)
    title_AR = models.CharField(max_length=255, null=False)
    is_delete=models.SmallIntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Hospital'

class Specilization(models.Model):
    title_EN= models.CharField(max_length=255, null=False)
    title_AR = models.CharField(max_length=255, null=False,default='')
    is_delete=models.SmallIntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Specilization'
