from django.core.validators import EmailValidator
from django.db import models
from django.utils.text import slugify


class Question(models.Model):
    langs=(
        ('fa','Farsi'),
        ('en','English'),
        ('tr','Turkish'),
    )
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name="date published")
    name = models.CharField(max_length=200, default="", blank=True)
    email = models.EmailField(max_length=200, default="", blank=True, help_text="Email address of creator of the question")
    language = models.CharField(max_length=200, choices=langs, default="en")
    q_slug = models.CharField(max_length=200, default="", blank=True, unique=True, editable=False)
    icon = models.ImageField(upload_to="polls/images/", null=True, blank=True)

    def __str__(self):
        return self.question_text

    def check_gmail(self):
        return "gmail" in self.email

    def save(self, **kwargs):
        self.q_slug = slugify(self.question_text)
        super().save(**kwargs)

    class Meta:
        db_table = "questions"
        verbose_name = "سوال"
        verbose_name_plural = "سوالها"
        ordering = ['-pub_date']


class Choice(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, to_field='q_slug')
    question = models.ManyToManyField(Question, through="ChoiceToQuestion")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class ChoiceToQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    date_votes = models.DateTimeField()


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    message = models.TextField()
