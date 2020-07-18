from django.conf.urls import url
from django.urls import path
from .views import DiaryView

urlpatterns = [
    # name は views.py 以下の関数に合わせる
    # name と 第2引数は合わせる
    # path("", views.index, name="index"),
    path("", DiaryView.form, name="form"),
    path("taiseiyo/", DiaryView.taiseiyo, name="taiseiyo"),  # 追記
]
