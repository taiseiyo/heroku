#!/usr/bin/env python3
from django.conf.urls import url
from django.urls import path
from .views import DiaryView
from .views import RegisterView
from . import views

urlpatterns = [
    path("", DiaryView.as_view(), name="form"),

    path("taiseiyo/", views.taiseiyo, name="taiseiyo"),  # 追記
    path("create/", RegisterView.as_view(), name="create"),
    path("edit/<int:num>", views.edit, name="edit"),
    path("delete/<int:num>", views.delete, name="delete"),
    path("restrict/<int:num>", views.restrict, name="restrict"),
    path("index2/", views.index2, name="index2"),
    path("3d/", views.three_d, name="3d"),
    path("bingo/", DiaryView.as_view(), name="bingo"),
    path("marubatu/", DiaryView.as_view(), name="marubatu"),

    # path("edit/<str:name>", views.edit, name="edit"),
]
