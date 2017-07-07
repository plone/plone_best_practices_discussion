# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import os

version = '0.1.dev0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='plone_best_practices_discussion',
    version=version,
    description="This is just a placehoder for a discussion about Plone best practices.",
    long_description=(read('README.rst') + '\n' +
                      read('docs', 'CONTRIBUTORS.rst')),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='web plone zope skeleton project',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/plone/plone_best_practices_discussion',
    license='GPL version 2',
    # packages=find_packages('src', exclude=['ez_setup']),
    # package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={
    },
    entry_points={},
)
