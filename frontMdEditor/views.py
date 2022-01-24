from django.shortcuts import render
from .forms import CreateFrontMdForm
from firstHtml.models import ExampleModel
from django.http import HttpResponseRedirect
from django.urls import reverse

def createMdPage(request):
    form = CreateFrontMdForm()
    result = {'form': form}
    return render(request, 'frontMdEditor/test.html', result)

def addPage(request):
    exampleModel = ExampleModel(name="test1")
    exampleModel.content = request.POST.get('form.fields.content')
    exampleModel.save()
    return HttpResponseRedirect(reverse('polls:index'))