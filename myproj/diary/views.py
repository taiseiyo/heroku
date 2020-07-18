#!/usr/bin/env python3
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import DailyForm
from django.views.generic import TemplateView


class DiaryView(TemplateView):

    def __init__(self):
        self.params = {
            "title": "Welcome to Diary Application Form",
            "message": "Input your data",
            "form": DailyForm()
        }

    def get(self, request):
        return render(request, "diary/taisei/form.html", self.params)

    def post(self, request):

        if(request.POST["name"] == "taiseiyo" and request.POST["password"] == "FGxG9wei"):
            template = loader.get_template('diary/taisei/index.html')
            return HttpResponse(template.render(None, request))

        return render(request, "diary/taisei/form.html", self.params)

    # def index(self, request):
    #     template = loader.get_template('diary/taisei/index.html')
    #     return HttpResponse(template.render(None, request))


def taiseiyo(request):  # 新しくnew関数を追記
    template_name = "diary/taisei/new.html"
    return render(request, template_name)
