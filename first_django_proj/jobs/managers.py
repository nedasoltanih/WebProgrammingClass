from django.db import models

class JobSeekerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='J')

class EmployerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='E')

class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(is_superuser='True')