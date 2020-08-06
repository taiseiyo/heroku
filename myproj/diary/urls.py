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
    # path("edit/<str:name>", views.edit, name="edit"),
]
