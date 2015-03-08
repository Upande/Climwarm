from django.views.generic import View, TemplateView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from AfricasTalkingGateway import *

class DefaultView(TemplateView):
	template_name = 'default.html'

class DroughtView(TemplateView):
	template_name = 'drought_hazard.html'

	def post(self, request, *args, **kwargs):
		try:
			import urllib2
			import simplejson
			req = urllib2.Request('http://maps.virtualkenya.org/geoserver/wfs?srsName=EPSG%3A4326&typename=geonode%3Adrought_constituencies&outputFormat=json&version=1.0.0&service=WFS&request=GetFeature')
			opener = urllib2.build_opener()
			f = opener.open(req)
			data = simplejson.load(f)
			gateway = AfricasTalkingGateway('upande', '5da433821fa3efe8d793bfb95da80e63a4f2909c559ea58cc5a8e096fa568965')
			for item in data['features']:
				msisdn = item['properties']['SNIPPET']
				print msisdn
				gateway.sendMessage(msisdn, 'Drought alert SMS from Early Warning System')
			gateway.sendMessage('+254722659526', 'Drought alert SMS from Early Warning System')
		except Exception as ex:
			print 'exception: {0}'.format(ex.message)
			pass
			
		return redirect(reverse('drought_home'))

class FloodView(TemplateView):
	template_name = 'flood_hazard.html'

	def post(self, request, *args, **kwargs):
		return redirect('drought_home')
