# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django-registration-pv',
    version='0.0.1',
    author=u'Joshua Tauberer',
    author_email=u'jt@occams.info',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/JoshData/django-registration-pv',
    license='CC0 (copyright waived)',
    description='A reusable Django app for new user registration with support for OpenID/OAuth login',
    long_description=open("README.md").read(),
    keywords="django registration openid oauth",
    install_requires=["django-picklefield"],
)
