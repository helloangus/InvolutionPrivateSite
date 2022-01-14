"""InvolutionPrivateSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import include, path
from firstHtml import views as firstviews

urlpatterns = [
    path('msggate/', include('msgapp.urls')),
    path('firstHtml/', include('firstHtml.urls')),  # 表示当访问firstHtml/时，去找本地路由
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', firstviews.homeproc)
]