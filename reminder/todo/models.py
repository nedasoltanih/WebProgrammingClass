from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()          # تاریخ سررسید
    due_time = models.TimeField()          # ساعت سررسید
    done = models.BooleanField(default=False)  # انجام شده یا نه
