from django.contrib import admin



# Register your models here.
from models import FAQTopic

admin.site.register(FAQTopic)



# class HomeSlideAdmin(admin.TabularInline):
#     model = HomeSlide
#
#     def get_extra(self, request, obj=None, **kwargs):
#         extra = 2
#         # if obj:
#         #     return extra - obj.binarytree_set.count()
#         return extra

# class HomeSlideAdmin(admin.StackedInline):
#
#     model = HomeSlide
#     max_num = 9
#
#
# class HomeCarouselAdmin(SingletonModelAdmin): #admin.ModelAdmin):
#
#     model = HomeCarousel
#
#     inlines = (HomeSlideAdmin, )
#
#     # class Meta:
#     #     verbose_name_plural = "ok"
#
#
#admin.site.register(HomeCarousel, HomeCarouselAdmin)
#admin.site.register(HomeSlide)

from solo.admin import SingletonModelAdmin
from models import HomeCarousel, HomeSlide


from django import forms
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin


class HomeSlideFormSet(BaseInlineFormSet):
    '''
    Validate formset data here
    '''
    def clean(self):
        super(HomeSlideFormSet, self).clean()

        #percent = 0
        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue
            data = form.cleaned_data
            #percent += data.get('percent', 0)
            print data
        # if percent != 100:
        #     raise ValidationError(_('Total of elements must be 100%%. Current : %(percent).2f%%') % {'percent': percent})

class HomeSlideAdmin(admin.TabularInline):
    model = HomeSlide
    formset = HomeSlideFormSet

class HomeCarouselAdmin(SingletonModelAdmin):
    inlines = (HomeSlideAdmin,)

admin.site.register(HomeCarousel, HomeCarouselAdmin)