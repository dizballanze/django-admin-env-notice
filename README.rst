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

Requirements
-----------

- Python 2.7, 3.4+
- Django 1.9+


Quickstart
----------

Install django-admin-env-notice::

    pip install django-admin-env-notice

Add it to your `INSTALLED_APPS` before `django.contrib.admin`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_admin_env_notice',
        'django.contrib.admin',
        ...
    )

Add context processor:

.. code-block:: python

    TEMPLATES = [
        {
            ...
            "OPTIONS": {
                "context_processors": [
                    ...
                    "django_admin_env_notice.context_processors.from_settings",
                ],
            },
        },
    ]

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
