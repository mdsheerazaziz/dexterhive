from django.conf.urls import url
from dexterhive.groups import views

urlpatterns = [
    url(r'^create-group/', views.create_group),
]