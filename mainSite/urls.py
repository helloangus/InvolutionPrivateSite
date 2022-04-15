from django.urls import path, re_path
from InvolutionPrivateSite.settings import MEDIA_ROOT
from django.views.static import serve
from . import views

app_name = 'mainSite'

urlpatterns = [
    path('', views.mainProc),
    path('<int:project_id>/', views.prj_detail, name='prj_detail'),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root":MEDIA_ROOT}),
]
