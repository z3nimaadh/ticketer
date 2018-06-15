from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/$', views.send_data, name='send_data'),
    
]
