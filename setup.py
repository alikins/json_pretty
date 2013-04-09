# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name="json_pretty",
    license="GPLv3",
    version='1.0',
    description="pretty print and colorize json",
    author="Adrian Likins",
    author_email="alikins@redhat.com",
    maintainer="Adrian Likins",
    maintainer_email="alikins@redhat.com",
    url="http://github.com/alikins/json_pretty",
    packages=["json_pretty"],
    install_requires=[
        "pygments == 1.6",
    ],
    entry_points={
        'console_scripts': ['json_pretty = json_pretty.json_pretty:main'],
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
    ],
)
