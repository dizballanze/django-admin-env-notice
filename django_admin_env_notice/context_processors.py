from django.conf import settings


def show_notice(request):
    return request.user.is_authenticated or getattr(settings, 'ENVIRONMENT_SHOW_TO_UNAUTHENTICATED', True)


def from_settings(request):
    return {
        'ENVIRONMENT_NAME': getattr(settings, 'ENVIRONMENT_NAME', None),
        'ENVIRONMENT_COLOR': getattr(settings, 'ENVIRONMENT_COLOR', None),
        'ENVIRONMENT_TEXT_COLOR': getattr(settings, 'ENVIRONMENT_TEXT_COLOR', "white"),
        'ENVIRONMENT_ADMIN_SELECTOR': getattr(
            settings, 'ENVIRONMENT_ADMIN_SELECTOR', 'body'),
        'ENVIRONMENT_FLOAT': getattr(settings, 'ENVIRONMENT_FLOAT', False),
        'show_notice': show_notice(request),

    }
