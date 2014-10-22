from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from views import landing

urlpatterns = patterns('faq.views',
    url(_(r'^dual_language/$'), landing, name='duallang_landing'),
)
