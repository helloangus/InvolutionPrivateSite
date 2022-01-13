from django.shortcuts import render

# 新增返回一个html页面的函数
def hello(request):
    return render(request, "test.html")