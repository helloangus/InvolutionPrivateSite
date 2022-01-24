from django.urls import path
from . import views

app_name = 'frontMdEditor'
urlpatterns = [
    path('', views.createMdPage, name='createMdPage'),
    path('addPage/', views.addPage, name='addPage'),
]