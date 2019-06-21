# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from polls.models import Question

from django.core.exceptions import ObjectDoesNotExist
from django.views.defaults import page_not_found

# Create your views here.
#def index(request):
#   return HttpResponse("Hello, world. Youŕe at he polls index.")


def nosotros(request):
    return HttpResponse('<h1 style="text-center;color:steelblue">Sección de nosotros</h1>')

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id )

def index(request):
   try:
      latest_question_list = Question.objects.order_by('-pub_date')[:4]
      #latest_question_list = Question.objects.all()
   except ObjectDoesNotExist:
      latest_question_list = {'question_text','error'} 
   template = loader.get_template('polls/index.html')
   context = {
      'latest_question_list' : latest_question_list
   }
 
   return HttpResponse(template.render(context))
   #return render(request, 'polls/index.html',context)
    #return HttpResponse('hola index')


