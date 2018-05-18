#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='tinycolor.py',
    version='0.1.0',

    author='WenryXu',
    author_email='wenryxu@outlook.com',

    description='tinycolor.py 是一个用于 Python 的颜色操作和转换的库。它支持多种形式的输入，同时提供颜色转换和一些其他的实用功能。',
    long_description='tinycolor.py 是一个用于 Python 的颜色操作和转换的库。它支持多种形式的输入，同时提供颜色转换和一些其他的实用功能。',
    keywords='Python TinyColor Color',

    url='https://github.com/WenryXu/tinycolor.py',
    license="MIT License",

    platforms='MacOS Linux Windows',

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'tinycolor.py=tinycolor.__main__:main'
        ]
    }
)
