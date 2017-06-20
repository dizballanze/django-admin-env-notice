from django.conf import settings


def from_settings(request):
    return {
        'ENVIRONMENT_NAME': getattr(settings, 'ENVIRONMENT_NAME', None),
        'ENVIRONMENT_COLOR': getattr(settings, 'ENVIRONMENT_COLOR', None),
    }
