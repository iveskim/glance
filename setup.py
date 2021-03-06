#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
from setuptools import setup, find_packages

NAME = "cpsglance"
DESCRIPTION = "CPS Glance"
URL = "git@git.jd.com:CPS/cps-ironic-parent.git"
EMAIL = "cloudid@jd.com"
AUTHOR = "JD Cloud Pysical System"
REQUIRES_PYTHON = ">=2.7"
VERSION = None

# What packages are required for this module to be executed?
INSTALL_REQUIRED = [
    "clint==0.5.1",
    "mock==2.0.0",
    "monotonic==1.5",
    "netaddr==0.7.19",
    "netifaces==0.10.7",
    "pika==0.12.0",
    "PyYAML==4.2b4",
    "pyparsing==2.2.2",
    "pyudev==0.21.0",
    "pint==0.8.1",
    "psutil==5.4.7",
    "requests==2.19.1",
    "six==1.11.0",
    "validators==0.12.2",
    "Jinja2==2.10"
]

DEPENDENCY_LINKS = [

]


here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if "README.md" is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except IOError:
    try:
        with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
            long_description = "\n" + f.read()
    except IOError:
        try:
            with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
                long_description = "\n" + f.read()
        except IOError:
            long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name = NAME,
    version = about["__version__"],
    description = DESCRIPTION,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = AUTHOR,
    author_email = EMAIL,
    platforms = "any",
    python_requires = REQUIRES_PYTHON,
    url = URL,
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires = INSTALL_REQUIRED,
    dependency_links = DEPENDENCY_LINKS,
    include_package_data = True,
    test_suite="nose.collector",
    tests_require=["nose"],
    license = "JDL",
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Natural Language :: Chinese",
        "License :: JD Approved :: JD Cloud Pysical System License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    zip_safe = False
)
