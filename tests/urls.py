# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_admin_env_notice.urls import urlpatterns as django_admin_env_notice_urls

urlpatterns = [
    url(r'^', include(django_admin_env_notice_urls, namespace='django_admin_env_notice')),
]
