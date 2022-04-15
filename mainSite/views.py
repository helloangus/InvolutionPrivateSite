from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from django.utils import timezone
from InvolutionPrivateSite.settings import MEDIA_ROOT
from django.contrib.auth.models import User

from .models import Project, UserInfo, Article


# 用户发布prj数量排名
def prj_rank():
    # 获取用户数量
    user_num = User.objects.all().count()
    # 建立用户发表项目数量的字典
    user_prj_num = {}
    # 统计每个用户发表的项目数量
    for user in User.objects.all():
        user_prj_num[user] = Project.objects.filter(user=user).count()

    # 根据用户发表项目数量从高到底排序
    user_prj_num = sorted(user_prj_num.items(), key=lambda x: x[1], reverse=True)

    # 返回排名前10的用户
    return user_prj_num[:10]

# 主站页面内容替换
def mainProc(request):
    # 再所有模板路径下搜索模板
    template = get_template("mainSite/homePage.html")

    latest_prj = Project.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:1].get()

    # 获取排名前10的用户
    user_prj_num = prj_rank()
    # 根据排名前10的用户，获取用户名字
    user_name = []
    for user in user_prj_num:
        user_name.append(user[0].username)

    # 获取最近的10篇文章
    article_list = Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

    # 字典类型，与html文件中的模板语言定义的变量替换
    context = {
        "latest_prj": latest_prj,
        "user_name": user_name,
        "article_list": article_list,
    }

    html = template.render(context)

    return HttpResponse(html)

# 显示项目详情
def prj_detail(request, project_id):
    # 在Project中寻找最新的，未找到则给出404错误
    project = get_object_or_404(Project.objects.filter(pub_date__lte=timezone.now()), pk=project_id)
    userInfo = UserInfo.objects.get(user=project.user)

    # 获取projectPage.html模板，展示项目详情
    template = get_template('mainSite/projectPage.html')
    context = {'project': project, 'userInfo': userInfo}
    response = HttpResponse(template.render(context, request))
    return response

# 显示文章详情
def article_detail(request, article_id):
    # 在Project中寻找最新的，未找到则给出404错误
    article = get_object_or_404(Article.objects.filter(pub_date__lte=timezone.now()), pk=article_id)
    userInfo = UserInfo.objects.get(user=article.user)

    # 获取projectPage.html模板，展示项目详情
    template = get_template('mainSite/articlePage.html')
    context = {'article': article, 'userInfo': userInfo}
    response = HttpResponse(template.render(context, request))
    return response


# 显示个人详情
def personal_detail(request, name):
    # 在User中寻找对应名字，未找到则给出404错误
    user = get_object_or_404(User, username=name)
    userInfo = UserInfo.objects.get(user=user)
    project_list = Project.objects.filter(pub_date__lte=timezone.now(), user=user).order_by('-pub_date')[:10]
    article_list = Article.objects.filter(pub_date__lte=timezone.now(), user=user).order_by('-pub_date')[:10]

    # 获取personalPage.html模板，展示个人详情
    template = get_template('mainSite/personalPage.html')
    context = {
        'user': user,
        'userInfo': userInfo,
        'project_list': project_list,
        'article_list': article_list,
        }
    response = HttpResponse(template.render(context, request))
    return response
