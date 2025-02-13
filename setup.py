#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install

VERSION = '1.5.0'


class VerifyVersionCommand(install):
    description = 'verify that git tag matches VERSION prior to publishing to pypi'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = 'Git tag: {0} does not match the version of this app: {1}'.format(
                tag, VERSION
            )
            sys.exit(info)


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


pandas = [
    'pandas>=0.24.0'
]

setup(
    name='enverus-developer-api',
    version=VERSION,
    description='Enverus Direct Access Developer API Python Client',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Cole Howard',
    author_email='wchatx@gmail.com',
    url='https://github.com/enverus-ea/enverus-developer-api',
    license='MIT',
    keywords=['enverus', 'drillinginfo', 'oil', 'gas'],
    packages=find_packages(exclude=('test*', )),
    package_dir={'enverus_developer_api': 'enverus_developer_api'},
    install_requires=['requests>=2.5.1, <3', 'unicodecsv==0.14.1'],
    extras_require={'pandas': pandas},
    cmdclass={
        'verify': VerifyVersionCommand,
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ]
)
