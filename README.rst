=============================
django-admin-env-notice
=============================

.. image:: https://badge.fury.io/py/django-admin-env-notice.svg
    :target: https://badge.fury.io/py/django-admin-env-notice

.. image:: https://travis-ci.org/dizballanze/django-admin-env-notice.svg?branch=master
    :target: https://travis-ci.org/dizballanze/django-admin-env-notice

.. image:: https://codecov.io/gh/dizballanze/django-admin-env-notice/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dizballanze/django-admin-env-notice

Visually distinguish environments in Django Admin

Documentation
-------------

The full documentation is at https://django-admin-env-notice.readthedocs.io.

Quickstart
----------

Install django-admin-env-notice::

    pip install django-admin-env-notice

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_admin_env_notice.apps.DjangoAdminEnvNoticeConfig',
        ...
    )

Add django-admin-env-notice's URL patterns:

.. code-block:: python

    from django_admin_env_notice import urls as django_admin_env_notice_urls


    urlpatterns = [
        ...
        url(r'^', include(django_admin_env_notice_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
