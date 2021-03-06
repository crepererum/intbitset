# -*- coding: utf-8 -*-
#
# This file is part of intbitset
# Copyright (C) 2013, 2014, 2015 CERN.
#
# intbitset is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# intbitset is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with intbitset; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""C-based extension implementing fast integer bit sets."""

from setuptools import Extension, setup

setup(
    name='intbitset',
    version='2.2.0.dev20150222',
    url='http://github.com/inveniosoftware/intbitset/',
    license='GPLv2',
    author='Invenio collaboration',
    author_email='info@invenio-software.org',
    description=__doc__,
    long_description=open('README.rst').read(),
    package_dir={'': 'src'},
    py_modules=['intbitset_helper'],
    ext_modules=[
        Extension("intbitset",
                  ["src/intbitset.c", "src/intbitset_impl.c"],
                  extra_compile_args=['-O3', '-march=native']
                  # For debug -> '-ftree-vectorizer-verbose=2'
                  )
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        "six",
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        # 'Development Status :: 5 - Production/Stable',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
