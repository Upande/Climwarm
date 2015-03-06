from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect

class DefaultView(TemplateView):
	template_name = 'default.html'

class DroughtView(TemplateView):
	template_name = 'drought_hazard.html'

	def post(self, request, *args, **kwargs):
		return redirect('drought_home')

class FloodView(TemplateView):
	template_name = 'flood_hazard.html'

	def post(self, request, *args, **kwargs):
		return redirect('drought_home')
