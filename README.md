# django-admin-env-notice

[![Package Version](https://badge.fury.io/py/django-admin-env-notice.svg)](https://badge.fury.io/py/django-admin-env-notice)
[![Build Status](https://travis-ci.org/dizballanze/django-admin-env-notice.svg?branch=master)](https://travis-ci.org/dizballanze/django-admin-env-notice)
[![Code Coverage](https://codecov.io/gh/dizballanze/django-admin-env-notice/branch/master/graph/badge.svg)](https://codecov.io/gh/dizballanze/django-admin-env-notice)

Visually distinguish environments in Django Admin. Based on great advice from post: [5 ways to make Django Admin safer](https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8) by [hakibenita](https://hackernoon.com/@hakibenita).

## Requirements

- Python 2.7, 3.4+
- Django 1.9+


## Quickstart

Install django-admin-env-notice::

```
pip install django-admin-env-notice
```

Add it to your `INSTALLED_APPS` before `django.contrib.admin`:

```python

INSTALLED_APPS = (
    ...
    'django_admin_env_notice',
    'django.contrib.admin',
    ...
)
```

Add context processor:

```python

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
```

Set label and color for current environment:

```python
ENVIRONMENT_NAME = "Production server"
ENVIRONMENT_COLOR = "#FF2222"
```

Override django admin selector if necessary (default: body), e.g: grappelli:

```python
ENVIRONMENT_ADMIN_SELECTOR = "grp-header"
```

Optionally, set the environment banner to float over instead of being fixed to the top:

```python
ENVIRONMENT_FLOAT = True
```

You can also set the text color (default: white) by setting:
```python
ENVIRONMENT_TEXT_COLOR = "#00FF00"
```

You can stop showing the banner to unauthenticated users by setting (default: `True`):
 
```python
ENVIRONMENT_SHOW_TO_UNAUTHENTICATED = False
```

## Screenshots

![](./screenshots/prod.png)
![](./screenshots/dev.png)
![](./screenshots/testing.png)

## Running Tests

Does the code actually work?

```
source <YOURVIRTUALENV>/bin/activate
(myenv) $ pip install tox
(myenv) $ tox
```

## Credits

Tools used in rendering this package:

- [Cookiecutter](https://github.com/audreyr/cookiecutter)
- [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
