#!/usr/bin/env python3
from django.conf.urls import url
from django.urls import path
from .views import DiaryView
from .views import RegisterView
from . import views

urlpatterns = [
    # name は views.py 以下の関数に合わせる
    # name と 第2引数は合わせる
    # path("", views.index, name="index"),
    path("", DiaryView.as_view(), name="form"),
    path("taiseiyo/", views.taiseiyo, name="taiseiyo"),  # 追記
    path("create/", RegisterView.as_view(), name="create"),
]
