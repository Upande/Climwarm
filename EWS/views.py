from django.views.generic import TemplateView

class DefaultView(TemplateView):
	template_name = 'default.html'

class HomeView(TemplateView):
	template_name = 'home.html'


class DroughtView(TemplateView):
	template_name = 'drought_hazard.html'

class FloodView(TemplateView):
	template_name = 'flood_hazard.html'