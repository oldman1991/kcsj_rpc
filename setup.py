# coding: utf-8
""" 
@author: oldman
@file: setup.py 
@time: 2020-04-27 13:25
"""

from setuptools import setup, find_packages

setup(
    name='kcsj_rpc',
    version='0.0.1',
    keywords='kcsj rpc',
    description='a library for rpc request Developer',
    author='oldman li',
    author_email='',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=["requests==2.31.0"],
)
