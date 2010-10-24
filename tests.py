"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from quizzes.models import Quiz

class SimpleTest(TestCase):
    def test_basic_addition(self):

        fail = Quiz.objects.create(title="Canadian Cities and Provinces")

        self.failUnlessEqual(fail, 1)


