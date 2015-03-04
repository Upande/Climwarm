from django.views.generic import TemplateView

class DefaultView(TemplateView):
	template_name = 'default.html'

class HomeView(TemplateView):
	template_name = 'home.html'