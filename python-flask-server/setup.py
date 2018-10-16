# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="SunVibe API",
    author_email="apiteam@sunvibe.vn",
    url="",
    keywords=["Swagger", "SunVibe API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    SunVibe is a Solar Energy Platform where small investors - crowd founders - together finance solar panel installation on the roof of other people’s - roof lenders - house. The installation is constructing by authorized Installers, but the quality assurance and monitoring done by SunVibe.  version: \&quot;0.1.0\&quot; 
    """
)

