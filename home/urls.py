from django.conf.urls import patterns, url

from views import landing

urlpatterns = patterns('home.views',
    url(r'^$', landing, name='home'),
)
