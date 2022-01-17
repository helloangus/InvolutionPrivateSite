from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse, Http404

from polls.models import Question



def index(request):
    template = get_template("index.html")

    # 从Question模型中获取按时间倒序排列的前五项记录，
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    response = HttpResponse(template.render(context, request))

    return response


def detail(request, question_id):
    # 在Question中寻找匹配question_id的question，未找到则给出404错误
    question = get_object_or_404(Question, pk=question_id)

    template = get_template('detail.html')
    context = {'question_id': question_id, 'question': question}
    response = HttpResponse((template.render(context, request)))
    return response

def results(request, question_id):
    response = HttpResponse()
    response.write("You are looking at the results of question %s." % question_id)
    return response

def vote(request, question_id):
    response = HttpResponse()
    response.write("You are voting on question %s." % question_id)
    return response