#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import codecs
from setuptools import setup, find_packages

NAME = 'jp_autotag'
DESC = 'simple tag correction for dump players'
VERSION = "0.0"
AUTHOR = 'Pierre Bayerl'
LICENSE = 'MIT'
URL = 'https://github.com/goto40/jp_autotag'
README = codecs.open(os.path.join(os.path.dirname(__file__), 'README.rst'),
                     'r', encoding='utf-8').read()


if sys.argv[-1].startswith('publish'):
    if os.system("pip list | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip list | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    if sys.argv[-1] == 'publishtest':
        os.system("twine upload -r test dist/*")
    else:
        os.system("twine upload dist/*")
        print("You probably want to also tag the version now:")
        print("  git tag -a {0} -m 'version {0}'".format(VERSION))
        print("  git push --tags")
    sys.exit()

mypackages = find_packages()
print("packages = {}".format(mypackages))

setup(
    name=NAME,
    version=VERSION,
    description=DESC,
    long_description=README,
    author=AUTHOR,
    maintainer=AUTHOR,
    license=LICENSE,
    url=URL,
    packages=mypackages,
    install_requires=["exeD3"],
    keywords="mp3 tag",
    entry_points={
        'console_scripts': [
            'jp_autotag = jp_autotag:autotag'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ]

)
