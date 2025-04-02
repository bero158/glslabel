# coding: utf-8

"""
    GLS API CLI

    CLI and classes for MyGLS services

"""  


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

NAME = "glslabel"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
    "dynaconf",
    "argparse",
    "PyPDF2",
    # "glslabelapi",
    "win32printing"
]

setup(
    name=NAME,
    version=VERSION,
    description="GLS API CLI",
    author="Eclipse print a.s.",
    author_email="beran@eclipse-print.com",
    url="",
    keywords=["GLS", "CLI", "MyGLS API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    CLI and classes for MyGLS services
    """,  
    package_data={"glslabelapi": ["py.typed"]},
)
