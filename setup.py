#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import platform
import os

NAME = 'MaratXBomber'
DESCRIPTION = 'SMS Bomber by MARAT'
URL = 'https://github.com/ByMline/MaratXBomber'
EMAIL = ''
AUTHOR = 'MaratMuratov'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '2.0.0'
REQUIRED = [
    "starlette", "aiofiles", "jinja2", "python-multipart", "fake_useragent",
    "uvicorn", "click",
    "aiohttp"
]
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['marat'],

    entry_points={
        'console_scripts': ['marat=marat.__main__:main'],
    },
    install_requires=REQUIRED,
    extras_require={},
    package_data={
        'marat': ['static/*', 'templates/*', 'services/*']
    },
    license='Mozilla Public License 2.0',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
