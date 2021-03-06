from django.conf import settings
import os
SMS_TOKEN = getattr(settings, 'SMS_TOKEN', os.environ.get('SMS_TOKEN'))
EMAIL_HOST_USER = getattr(settings, 'EMAIL_HOST_USER',
                          os.environ.get('EMAIL_HOST_USER'))
