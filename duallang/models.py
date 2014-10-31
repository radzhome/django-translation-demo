from django.db import models
from django.utils.translation import ugettext_lazy as _

#from linguo.models import MultilingualModel
#from linguo.managers import MultilingualManager

from django.db import models
from solo.models import SingletonModel


class HomeCarousel(SingletonModel):

    # class Meta:
    #     verbose_name = 'Home Carousel'

    def __unicode__(self):
        return 'Home Carousel'


class HomeSlide(models.Model):

    carousel = models.ForeignKey(HomeCarousel)
    label = models.CharField(max_length=255, unique=True)
    text = models.TextField()


class FAQTopic(models.Model): #MultilingualModel):

    #All field labels and help text are translated
    name = models.CharField(_('name'), max_length=255, unique=True, help_text=_("Name of the FAQ Topic"))
    slug = models.SlugField(_('slug'))
    text = models.TextField(_('text field test'), help_text=_("This is a help text"))
    #order = models.PositiveSmallIntegerField(_('order'), default=0)
    #image = models.ImageField(_('icon'), blank=True, null=True, upload_to='faq/faqtopics/images')

    #objects = MultilingualManager()

    class Meta:
        verbose_name = _('faq topic')
        verbose_name_plural = _('faq topics')
        #translate = ('name', 'slug')  # for use with linguo package
        #ordering = ('order', 'id')

    def __unicode__(self):
        return self.name