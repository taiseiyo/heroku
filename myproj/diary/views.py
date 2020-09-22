#!/usr/bin/env python3
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .forms import DailyForm, RegisterForm, \
    Re_RegisterForm, RestrictForm
from .models import ActiveUser
from django.views.generic import TemplateView


class DiaryView(TemplateView):
    def __init__(self):
        # レコード(テーブルに保管されるデータ)の取得
        self.data = ActiveUser.objects.all().order_by("name", "mail")
        # ActiveUser.objects.all().delete()

        self.params = {
            "title": "Welcome to My_Application Form",
            "message": "Input your data",
            "form": DailyForm(),
            "data": self.data
        }

    def get(self, request):
        return render(request, "diary/taisei/form.html", self.params)

    def post(self, request):
        if(request.POST["name"] == "taiseiyo" and request.POST["password"] == "welcome"):
            template = loader.get_template('diary/taisei/index.html')
            return HttpResponse(template.render(None, request))

        elif(request.POST["name"] == "bingo" and request.POST["password"] == "welcome"):
            template = loader.get_template('diary/taisei/bingo.html')
            return HttpResponse(template.render(None, request))

        return render(request, "diary/taisei/form.html", self.params)


class RegisterView(TemplateView):
    def __init__(self):
        self.data = ActiveUser.objects.all().order_by("name", "mail")
        self.params = {
            "title": "Register your data",
            "form": RegisterForm(),
            "data": self.data
        }

    def get(self, request):
        return render(request, "diary/taisei/create.html", self.params)

    def post(self, request):
        if(len(request.POST["name"]) > 0 and len(request.POST["mail"]) > 0):
            active_user = ActiveUser(
                1 if len(self.data.values("name")) == 0 else len(self.data.values("name"))+1, request.POST["name"], request.POST["mail"])
            active_user.save()
            return redirect(to="form")
        return render(request, "diary/taisei/create.html", self.params)


def taiseiyo(request):  # 新しく new 関数を追記
    template_name = "diary/taisei/new.html"
    return render(request, template_name)


def edit(request, num):
    obj = ActiveUser.objects.get(id=num)
    # obj = ActiveUser.objects.get(name=name)
    if(request.method == "POST"):
        re_register = Re_RegisterForm(request.POST, instance=obj)
        re_register.save()
        return redirect(to="form")
    params = {
        "title": "Change information",
        "id": num,
        # "name": name,
        "form": Re_RegisterForm(instance=obj)
    }
    return render(request, "diary/taisei/edit.html", params)


def delete(request, num):
    active_user = ActiveUser.objects.get(id=num)
    if(request.method == "POST"):
        active_user.delete()
        return redirect(to="form")
    params = {
        "title": "Delete information",
        "id": num,
        "obj": active_user
    }
    return render(request, "diary/taisei/delete.html", params)


def restrict(request, num):
    active_user = ActiveUser.objects.get(id=num)
    params = {
        "title": "This operation is limited",
        "message": "Enter password",
        "id": num,
        "form": RestrictForm(),
        "obj": active_user
    }

    if(request.method == "POST"):
        if(request.POST["password"] == "FGxG9wei"):
            params["title"] = "Delete information"
            return render(request, "diary/taisei/delete.html", params)

    return render(request, "diary/taisei/restrict.html", params)


def index2(request):
    return render(request, "diary/taisei/index2.html")


def three_d(request):
    return render(request, "diary/taisei/3d.html")
