from django.db import models
from datetime import datetime
# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    number_of_random_question = models.IntegerField(max_length=4)
    pass_rate = models.IntegerField(max_length=4)
    summary_pass = models.TextField(blank=True)
    summary_default = models.TextField(blank=True)
    shuffle = models.BooleanField(default=False)
    backwards_navigation = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now)
    quiz_always = models.BooleanField(default=False)
    quiz_open = models.DateTimeField(default=datetime.now)
    quiz_close = models.DateTimeField(default=datetime.now)
    takes = models.IntegerField(max_length=4)
    time_limit = models.IntegerField(max_length=10)
    enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __unicode__(self):
        return self.title

class ResultOption(models.Model):
    quiz = models.ForeignKey(Quiz)
    name = models.CharField(max_length=255)
    summary = models.TextField(blank=True)
    start = models.IntegerField(max_length=4)
    end = models.IntegerField(max_length=4)

class Question(models.Model):
    quiz = models.ManyToManyField(Quiz)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class MultipleChoice(models.Model):
    question = models.ForeignKey(Question)
    answer = models.TextField(blank=True)
    feedback = models.TextField(blank=True)
    is_correct = models.BooleanField()

    def __unicode__(self):
        return self.question.title


