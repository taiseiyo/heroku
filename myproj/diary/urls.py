from django.conf.urls import url
from django.urls import path
from .views import DiaryForm

urlpatterns = [
    # name は views.py 以下の関数に合わせる
    # name と 第2引数は合わせる
    # path("", views.index, name="index"),
    path("", DiaryForm.form(), name="form"),
    path("taiseiyo/", DiaryForm.taiseiyo(), name="taiseiyo"),  # 追記
]
