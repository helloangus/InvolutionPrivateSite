from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    # 项目展示页的展示信息
    list_display = ('user', 'project_name', 'pub_date')
    list_filter = ['user', 'pub_date']
    search_fields = ['project_name']

    # 具体问题详情页的展示信息和风格
    fieldsets = [
        (None,               {'fields': ['project_name', 'user']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Content', {'fields': ['project_img', 'project_theme', 'project_content']}),
    ]


admin.site.register(Project, ProjectAdmin)
