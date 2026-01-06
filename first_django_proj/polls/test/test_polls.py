from django.utils import timezone

from django.test import TestCase, Client
from polls.models import *

class TestPolls(TestCase):

    @staticmethod
    def setUpTestData():
        Question.objects.create(question_text="Question 1", pub_date=timezone.now(), email="q1@gmail.com")
        Question.objects.create(question_text="Question 2", pub_date=timezone.now(), email="q2@ymail.com")

    def setUp(self):
        pass

    def test_gmail(self):
        q_gmail = Question.objects.get(question_text="Question 1")
        q_ymail = Question.objects.get(question_text="Question 2")

        self.assertTrue(q_gmail.check_gmail())
        self.assertFalse(q_ymail.check_gmail())

    def test_login(self):
        client = Client()
        response = client.post("/jobs/login/", {"username": "admin", "password": "123"})
        self.assertEqual(response.status_code, 404)
