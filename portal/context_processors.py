from django.conf import settings


def sitename(request):
    return {'sitename': settings.APP_NAME}
