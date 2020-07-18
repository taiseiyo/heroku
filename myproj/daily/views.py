#!/usr/bin/env python3
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import DailyForm


def form(request):
    params = {
        "titie": "日記",
        "message": "Input your data",
        "form": DailyForm()
    }

    if(request.method == "POST"):

        if(request.POST["name"] == "taiseiyo" and request.POST["password"] == "FGxG9wei"):
            template = loader.get_template('daily/taisei/index.html')
            return HttpResponse(template.render(None, request))

    return render(request, "daily/taisei/form.html", params)


def index(request):
    template = loader.get_template('daily/taisei/index.html')
    return HttpResponse(template.render(None, request))


def taiseiyo(request):  # 新しくnew関数を追記
    template_name = "daily/taisei/new.html"
    return render(request, template_name)
