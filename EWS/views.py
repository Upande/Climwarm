from django.views.generic import View, TemplateView

from .mixins import HazardAlertMixin
from .models import *


class DefaultView(TemplateView):
    template_name = 'default.html'


class Home(TemplateView):
    template_name = 'default2.html'


class CaseStudies(TemplateView):
    template_name = 'case_studies.html'

    def get_context_data(self, **kwargs):
        context = super(CaseStudies, self).get_context_data(**kwargs)
        tab = kwargs['tab']
        context.update(locals())
        return context

class Nzoia(TemplateView):
    template_name = 'nzoia.html'

    def get_context_data(self, **kwargs):
        context = super(Nzoia, self).get_context_data(**kwargs)
        readings = HazardReading.objects.all()
        print 'READINGS:'
        print readings
        context.update(locals())
        return context


class Kwale(TemplateView):
    template_name = 'kwale.html'

class Turkana(TemplateView):
    template_name = 'turkana.html'

class Ukame(TemplateView):
    template_name = 'drought_hazard_2.html'


class Mafuriko(TemplateView):
    template_name = 'flood_hazard_2.html'


class DroughtView(HazardAlertMixin, TemplateView):
    template_name = 'drought_hazard.html'
    hazard_type = 'Drought'
    sms_template = 'Alert: Drought risk for {0} (dek 3 March 2011) is worsening; a dry spell is expected with an early Alarm scenario developing in the course of wet season (March-May 2011).'
    email_template = 'Alert: Drought risk for {0} (dek 3 March 2011) is worsening; a dry spell is expected with an early Alarm scenario developing in the course of wet season (March-May 2011).'


class FloodView(HazardAlertMixin, TemplateView):
    template_name = 'flood_hazard.html'
    hazard_type = 'Flood'
    sms_template = 'Alert: Flood depths of up to 3m are predicted for large parts of Nzoia in the next 3 days, please contact all cooperating agencies.'
    email_template = 'Alert: Flood depths of up to 3m are predicted for large parts of Nzoia in the next 3 days, please contact all cooperating agencies.'
