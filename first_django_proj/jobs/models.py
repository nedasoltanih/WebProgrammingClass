from django.contrib.auth.models import AbstractUser, User
from django.core.mail import send_mail
from django.db import models
from .managers import EmployerManager,JobSeekerManager,MyManager

class Person (models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=1, choices={("J", "Jobseeker"), ("E", "Employer")})
    email = models.EmailField(null=True)
    code = models.CharField(max_length=6, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    employers = EmployerManager()
    jobseekers = JobSeekerManager()
    objects = MyManager()

    def __str__(self):
        return self.name

    # def save(self):
    #     super().save()
    #     send_mail(
    #         subject="Account created",
    #         message="Your account has been created",
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=[self.email]
    #     )



