from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    """Home page to Display all the questions"""
    questions_list = Question.objects.all().order_by('-pub_date')
    context = {'questions_list': questions_list}

    return render(request, 'polls/home.html', context)

def detail(request, question_id):
    return HttpResponse("Detials")

def results(request, question_id):
    return HttpResponse("results")

def vote(request, question_id):
    return HttpResponse("vote")