import os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template.loader import get_template


# 新增返回一个html页面的函数
def hello(request):
    return render(request, 'firstHtml/test.html')

# 首页信息
def homeproc(request):
    # response = HttpResponse()
    # response.write("<h1>This is the home page.</h1>")
    # response.write("For firstHtml, please click <a href='./testPage'>firstHtml</a>.<br>")
    # response.write("For msgapp, please click <a href='./msgapp'>msgapp</a>.<br>")
    # response.write("For polls, please click <a href='./polls'>polls</a>.<br>")
    # response.write("For 好康的, please click <a href='./video'>here</a>.<br>")
    # response.write("For 更好康的, please click <a href='./picture'>here</a>.<br>")
    
    # return response

    # 使用模板语言替换html文件中的内容
    # 在所有的模板路径下搜索模板
    template = get_template("firstHtml/homePage.html")
    # 字典类型，与html文件中模板语言定义的变量替换
    context = {"name1":"好康的", "name2":"更好康的", \
        "link1": "https://www.bilibili.com/video/BV1GJ411x7h7?share_source=copy_web", "link2": "./picture"}
    # 使用render方法渲染
    html = template.render(context)

    return HttpResponse(html)

# 流式响应-文件下载
def pictureDownload(request):
    cwd = os.path.dirname(os.path.abspath(__file__))
    response = FileResponse(open(cwd + "/static/images/haokangde.jpg", "rb"))

    # MIME标记
    response['Content-Type'] = 'application.octet-stream'   # 指定文件类型
    response['Content-Disposition'] = 'attachment;filename="haokangde.jpg"' # 注意这里是下载时的文件名，不可为中文
    return response

# def videoDownload(request):
#     cwd = os.path.dirname(os.path.abspath(__file__))
#     response = FileResponse(open(cwd + "/templates/You_have_been_deceived.mp4", "rb"))

#     # MIME标记
#     response['Content-Type'] = 'application.octet-stream'   # 指定文件类型
#     response['Content-Disposition'] = 'attachment;filename="You_have_been_deceived.mp4"' # 注意这里是下载时的文件名，不可为中文
#     return response
