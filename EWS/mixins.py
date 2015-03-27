from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


from AfricasTalkingGateway import *
import mandrill


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class HazardAlertMixin(object):
    hazard_type = 'HAZARD'
    sms_template = 'DEFAULT SMS Message'
    email_template = 'DEFAULT EMAIL Message'

    def post(self, request, *args, **kwargs):
        try:
            import urllib2
            import simplejson
            postdata = request.POST.copy()
            alert_type = postdata['alert_type']
            hazard_type = postdata['hazard_type']
            print 'ALERT TYPE: {0}'.format(alert_type)
            print 'HAZARD TYPE: {0}'.format(hazard_type)
            req = urllib2.Request('http://maps.virtualkenya.org/geoserver/wfs?srsName=EPSG%3A4326&typename=geonode%3Adrought_constituencies&outputFormat=json&version=1.0.0&service=WFS&request=GetFeature')
            opener = urllib2.build_opener()
            f = opener.open(req)
            data = simplejson.load(f)
            if (alert_type == 'SMS'):
                gateway = AfricasTalkingGateway('upande',
                        '5da433821fa3efe8d793bfb95da80e63a4f2909c559ea58cc5a8e096fa568965')
                for item in data['features']:
                    msisdn = item['properties']['SNIPPET']
                    locale = item['properties']['CONSTITUEN']
                    print msisdn
                    gateway.sendMessage(msisdn, self.sms_template.format(locale))
                gateway.sendMessage('+254722659526',
                        self.sms_template)
            elif (alert_type == 'EMAIL'):
                mandrill_client = mandrill.Mandrill('17dld1KJhCspkCV6zlfbtA')
                for item in data['features']:
                    to_list = []
                    email_address = item['properties']['SNIPPET2']
                    locale = item['properties']['CONSTITUEN']
                    message = {
                        'from_email': 'ews@upande.com',
                        'subject': '{0} early warning'.format(self.hazard_type),
                        'text': self.email_template.format(locale)
                    }
                    to_list.append(
                        {'email': email_address, 'name': locale, 'type': 'to'}
                    )
                message.update({'to': to_list})
                result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
                print result
        except Exception as ex:
            print 'exception: {0}'.format(ex.message)
            pass
        return redirect(reverse('drought_home'))
