from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # name は views.py 以下の関数に合わせる
    # name と 第2引数は合わせる
    # url('', views.index, name='index'),

    # url(r'^taiseiyo$',
    #     views.index, name='taiseiyo'),

    path("", views.index, name="index"),
    path("taiseiyo/", views.taiseiyo, name="taiseiyo"),  # 追記
]
