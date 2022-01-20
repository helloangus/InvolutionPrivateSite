from django.contrib import admin
from .models import ExampleModel



from django.db import models
from mdeditor.widgets import MDEditorWidget

class ExampleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    } 

admin.site.register(ExampleModel, ExampleModelAdmin)