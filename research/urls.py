from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^detail/(?P<eventId>\w+)/?', api_views.detail, name="eventdetail"),
    url(r'^upload/?', views.upload, name='dumpcontent'),
    url(r'^(?P<id>\d+)/?', views.index, name='researchbyid'),
    url(r'^', views.index, name='researchindex'),
]
