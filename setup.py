# -*- coding: utf-8 -*-

from setuptools import setup


def readme_file_contents():
    with open('README.rst')as readme_file:
        data=readme_file.read()


setup(
    name='J2SPOT',
    version='1.0.0',
    description='Simple TCP honeypot by team boyz.',
    long_description=readme_file_contents(),
    author='J2Spot',
    license='GPL-3.0',
    packages=['J2SPOT'],
    zip_safe=False,
    install_requires=[ ]
)
    return data
