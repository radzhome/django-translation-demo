
from django.views.generic import ListView

from models import FAQTopic


landing = ListView.as_view(template_name='dual_lang/landing.html',
    model=FAQTopic, context_object_name='topic_list')
