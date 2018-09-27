from django.conf.urls import url, include
from django.contrib import admin
from polls import views as polls_views
admin.autodiscover()

urlpatterns = [
    url('',polls_views.index, name='index')
]