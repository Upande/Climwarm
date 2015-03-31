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
            postdata = request.POST.copy()
            alert_type = postdata['alert_type']
            recipients = postdata['recipients']
            print 'ALERT TYPE: {0}'.format(alert_type)
            print 'RECS: {0}'.format(recipients)
            if (alert_type == 'SMS'):
                gateway = AfricasTalkingGateway('upande',
                        '5da433821fa3efe8d793bfb95da80e63a4f2909c559ea58cc5a8e096fa568965')
                for msisdn in recipients.split(','):
                    locale = 'Turkana'
                    print msisdn.strip()
                    gateway.sendMessage(msisdn.strip(), self.sms_template.format(locale))
                gateway.sendMessage('+254722659526',
                    self.sms_template)
            elif (alert_type == 'EMAIL'):
                mandrill_client = mandrill.Mandrill('17dld1KJhCspkCV6zlfbtA')
                locale = 'TURKANA'
                message = {
                    'from_email': 'ews@upande.com',
                    'subject': '{0} early warning'.format(self.hazard_type),
                    'text': self.email_template.format(locale)
                }
                to_list = []
                for recipient in recipients.split(','):
                    print recipient.strip()
                    to_list.append(
                        {'email': recipient.strip(), 'name': locale, 'type': 'to'}
                    )
                message.update({'to': to_list})
                result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
                print result
        except Exception as ex:
            print 'exception: {0}'.format(ex.message)
            pass
        return redirect(reverse('drought_home'))
