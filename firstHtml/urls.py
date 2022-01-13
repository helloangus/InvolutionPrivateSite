from django.urls import path
from . import views

# 新增路由请求
urlpatterns = [
    path('', views.hello)
]
