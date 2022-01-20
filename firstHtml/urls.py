from django.urls import path
from . import views

# 新增路由请求
app_name = 'firstHtml'
urlpatterns = [
    path('', views.markdown_detail),
]
