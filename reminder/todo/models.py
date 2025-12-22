from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()          # تاریخ سررسید
    due_time = models.TimeField()          # ساعت سررسید
    done = models.BooleanField(default=False)  # انجام شده یا نه
    category = models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.title

    @staticmethod
    def due_date_passed():
        return Task.objects.filter(due_date__lt=timezone.now(), done=False)

    def not_done(self):
        if self.due_date < timezone.now().date() and not self.done:
            return True
        return False
