from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.utils import timezone
from polls.models import Question, Choice



def index(request):
    template = get_template("polls/index.html")

    # 从Question模型中获取按时间倒序排列的前五项记录，
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    response = HttpResponse(template.render(context, request))

    return response


def detail(request, question_id):
    # 在Question中寻找匹配question_id的question，未找到则给出404错误
    question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()), pk=question_id)

    # 获取detail.html模板，展示问题内容和选项
    template = get_template('polls/detail.html')
    context = {'question_id': question_id, 'question': question}
    response = HttpResponse(template.render(context, request))
    return response

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = get_template('polls/results.html')
    context = {'question': question}
    response = HttpResponse(template.render(context, request))
    return response


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # 可能的异常处理
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 刷新页面，并给出错误信息
        template = get_template('polls/detail.html')
        context = {
            'question': question,
            'error_message': "You did not select a choice."
        }
        response = HttpResponse(template.render(context, request))
        return response
    else:
        # 若正常，用F()函数包裹，避免竞争条件
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # 成功处理POST请求后，都需要进行重定向
        return HttpResponseRedirect(reverse('polls:results', args = (question_id,)))