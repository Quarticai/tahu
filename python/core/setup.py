#!/usr/bin/env python
import codecs
import sys
import os
from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def read(*parts):
    path = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(path, encoding='utf-8') as fobj:
        return fobj.read()


def get_install_requires(requirement_file):
    requirements = read(requirement_file)
    install_requires = []
    for line in requirements.split('\n'):
        line = line.strip()
        if line and not line.startswith('-'):
            install_requires.append(line)
    return install_requires


setup(
    name='quartic-tahu',
    description='Tahu sparkplug constants',
    author='Quartic.ai Engineering Team',
    long_description=read('readme.txt'),
    long_description_content_type='text/markdown',
    author_email='tech@quartic.ai',
    url='https://github.com/Quarticai/tahu',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Tahu',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        ],
    install_requires=get_install_requires('requirements.in'),
    include_package_data=True,
    keywords='tahu',
    py_modules=['sparkplug_b', 'sparkplug_b_pb2'],
    package_data={
        # If any package contains *.so or *.pyi or *.lic files or *.key files,
        # include them:
        "": ["*.so", "*.pyi", "*.lic", "*.key"],
        }
    )
