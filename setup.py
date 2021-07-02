#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("LICENSE") as license_file:
    license = license_file.read()

requirements = [
    "Numpy>=1, <2",
    "opencv-python-headless>=4.3.0.38,<5",
    "numpy_indexed>=0.3.5, <0.4",
    "scipy>=1.4.1, <2",
    "scikit-image>=0.16.2, <1",
    "simplification>=0.4, <0.6",
]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    author="Tom Nijhof",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Tomni is a collection of image analysis functions usefull for CytoSmart solution.",
    entry_points={"console_scripts": ["tomni=tomni.cli:__init__"]},
    install_requires=requirements,
    long_description=readme + "\n\n" + history + "\n\n" + license,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="tomni",
    name="tomni",
    packages=find_packages(include=["tomni*"], exclude=["docs*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/cytosmart-bv/tomni",
    version="1.7.3",
    zip_safe=False,
)
