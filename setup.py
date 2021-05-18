#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    """Return the README file contents. Supports text,rst, and markdown"""
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file(name)
    return ''

__import__('django_admin_env_notice')


version = sys.modules['django_admin_env_notice'].get_version().replace(' ', '-')


setup(
    name='django-admin-env-notice',
    version=version,
    description="""Visually distinguish environments in Django Admin""",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    author='Iurii Shikanov',
    author_email='dizballanze@gmail.com',
    url='https://github.com/dizballanze/django-admin-env-notice',
    packages=[
        'django_admin_env_notice',
    ],
    include_package_data=True,
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords='django-admin-env-notice',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
