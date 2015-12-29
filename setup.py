#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

description = """
PostgreSQL json field support for Django.
"""

setup(
    name="pgjson",
    version="0.0.1",
    url="https://github.com/aymankh86/pgjson",
    license="BSD",
    platforms=["OS Independent"],
    description=description.strip(),
    author="Ayman Khalil",
    author_email="ayman.khalil33@gmail.com",
    keywords="django, postgresql, pgsql, json, field",
    maintainer="Ayman Khalil",
    maintainer_email="ayman.khalil33@gmail.com",
    packages=find_packages(),
    include_package_data=False,
    install_requires=[],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP",
    ]
)
