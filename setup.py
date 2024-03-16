"""
Setup script for the game package.

Note: This script is typically executed by running 'python setup.py install' to
install the package, or 'python setup.py develop' for a development install.

Examples-
    # To install the package:
    $ python setup.py install

    # To install the package in development mode:
    $ python setup.py develop.
"""
from setuptools import setup, find_packages

setup(
    name="game",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)