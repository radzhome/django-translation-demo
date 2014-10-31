from django.contrib import admin

from solo.admin import SingletonModelAdmin

# Register your models here.
from models import FAQTopic

admin.site.register(FAQTopic)

from models import HomeCarousel, HomeSlide


class HomeSlideAdmin(admin.StackedInline):

    model = HomeSlide
    max_num = 9


class HomeCarouselAdmin(SingletonModelAdmin): #admin.ModelAdmin):

    model = HomeCarousel

    inlines = (HomeSlideAdmin, )

    class Meta:
        verbose_name_plural = "ok"


admin.site.register(HomeCarousel, HomeCarouselAdmin)