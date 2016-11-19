from django.conf.urls import url
from dexterhive.calendars import views

urlpatterns = [
    url(r'^authorize-google-calendar/', views.get_authorization_url),
    url(r'^save-google-calendar-credentials/', views.save_credentials),
]