from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('daily/index.html')
    return HttpResponse(template.render(None, request))


def taiseiyo(request):  # 新しくnew関数を追記
    template_name = "daily/new.html"
    return render(request, template_name)
