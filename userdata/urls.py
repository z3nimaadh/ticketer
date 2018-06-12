from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.submit_page, name='submit_page'),
]
