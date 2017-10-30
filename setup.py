#!/usr/bin/env python

import Cython.Build
import numpy as np
from setuptools import setup, Extension


def get_version():
    """Load the version from version.py, without importing it.

    This function assumes that the last line in the file contains a variable defining the
    version string with single quotes.
    """
    with open('iodata/version.py', 'r') as fhandle:
        return fhandle.read().split('=')[-1].replace('\'', '').strip()


def get_readme():
    """Load README.rst for display on PyPI."""
    with open('README.rst') as fhandle:
        return fhandle.read()


setup(
    name='periodic',
    version=get_version(),
    description='',
    long_description=get_readme(),
    author='Toon Verstraelen',
    author_email='Toon.Verstraelen@UGent.be',
    url='https://github.com/theochem/periodic',
    package_dir={'iodata': 'iodata'},
    packages=['iodata', 'iodata.test'],
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Intended Audience :: Science/Research',
    ],
    zip_safe=False,
    setup_requires=['numpy>=1.0', ],
    install_requires=['numpy>=1.0', 'nose>=0.11', ],
)
