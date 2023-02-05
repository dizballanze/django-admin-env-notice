# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.urls import re_path
from django.contrib import admin


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
]
