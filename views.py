# Create your views here.

from django.template.context import RequestContext
from quizzes.models import Question
from django.shortcuts import render_to_response

def question(request, id, template_name='question.html'):

    question = Question.objects.get(multiplechoice__question__id = 1)
    answers  = question.multiplechoice_set.all()

    context = {'question':question, 'answers':answers}

    return render_to_response(template_name, context, context_instance=RequestContext(request))