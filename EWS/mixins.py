from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings


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
        case_study = ''
        try:
            postdata = request.POST.copy()
            alert_type = postdata['alert_type']
            recipients = postdata['recipients']
            if (alert_type == 'SMS'):
                if (postdata['sms_alert_message']):
                    self.sms_template = postdata['sms_alert_message']
                    case_study = postdata['return_url']
                gateway = AfricasTalkingGateway('upande',
                                                settings.AFRICAS_TALKING_API_KEY)
                for msisdn in recipients.split(','):
                    locale = 'Turkana'
                    gateway.sendMessage(
                        msisdn.strip(),
                        self.sms_template.format(locale)
                    )
                gateway.sendMessage('+254722659526',
                                    self.sms_template)
            elif (alert_type == 'EMAIL'):
                client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
                if (postdata['email_alert_message']):
                    self.email_template = postdata['email_alert_message']
                    case_study = postdata['return_url']
                template_content = [
                    {
                        'content': 'example content',
                        'name': 'ews_email_alert'
                    }
                ]
                locale = 'TURKANA'
                message = {
                    'from_email': 'ews@upande.com',
                    'global_merge_vars': [
                        {
                            'name': 'MESSAGE_TEXT',
                            'content': self.email_template.format(locale)
                        },
                        {
                            'name': 'HAZARD_TYPE',
                            'content': self.hazard_type
                        }
                    ]
                }
                to_list = []
                for recipient in recipients.split(','):
                    to_list.append(
                        {
                            'email': recipient.strip(),
                            'name': locale,
                            'type': 'to'
                        }
                    )
                message.update({'to': to_list})
                result = client.messages.send_template(
                    template_name='ews_email_alert',
                    template_content=template_content,
                    message=message, async=False,
                    ip_pool='Main Pool'
                )
                print result
        except Exception as ex:
            print 'exception: {0}'.format(ex.message)
            pass
        if(case_study != ''):
            return redirect(reverse(case_study))
        return redirect(reverse('drought_home'))
