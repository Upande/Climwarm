from django.views.generic import View, TemplateView

from .mixins import HazardAlertMixin

class DefaultView(TemplateView):
    template_name = 'default.html'


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
