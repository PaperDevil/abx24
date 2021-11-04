from distutils.core import setup
from setuptools import find_packages

from abx24 import __version__, __author__, __license__

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='abx24',
    version=__version__,
    install_requires=['aiohttp'],
    packages=find_packages(),
    url='https://github.com/paperdevil/bitrix24-python-rest',
    license=__license__,
    author=__author__,
    author_email='ketov-x@yandex.ru',
    description='Bitrix24 REST API wrapper provides easy way to communicate with bitrix24 portal over REST without OAuth',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='bitrix24 async api rest',
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
