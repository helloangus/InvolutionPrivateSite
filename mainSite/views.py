from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse


# 返回主站页面
def mainPage(request):
    return render(request, "homePage.html")

# 主站页面内容替换
def mainProc(request):
    # 再所有模板路径下搜索模板
    template = get_template("homePage.html")
    # 字典类型，与html文件中的模板语言定义的变量替换
    context = {
        "theme": "Test theme",
    }

    html = template.render(context)

    return HttpResponse(html)