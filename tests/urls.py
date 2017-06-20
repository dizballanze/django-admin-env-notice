# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
