from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from django.utils import timezone
from InvolutionPrivateSite.settings import MEDIA_ROOT

from .models import Project


# 主站页面内容替换
def mainProc(request):
    # 再所有模板路径下搜索模板
    template = get_template("mainSite/homePage.html")

    latest_prj = Project.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:1]
    # 字典类型，与html文件中的模板语言定义的变量替换
    context = {
        "latest_prj": latest_prj,
    }

    html = template.render(context)

    return HttpResponse(html)

# 显示项目详情
def prj_detail(request, project_id):
    # 在Project中寻找最新的，未找到则给出404错误
    project = get_object_or_404(Project.objects.filter(pub_date__lte=timezone.now()), pk=project_id)

    # 获取projectPage.html模板，展示项目详情
    template = get_template('mainSite/projectPage.html')
    context = {'project': project,}
    response = HttpResponse(template.render(context, request))
    return response