from django.conf.urls import url
from dexterhive.core import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^dashboard/$', views.dash_board)
]