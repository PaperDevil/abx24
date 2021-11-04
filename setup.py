from distutils.core import setup
from setuptools import find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='abx24',
    version='1.1.2',
    install_requires=['aiohttp'],
    packages=find_packages(),
    url='https://github.com/paperdevil/bitrix24-python-rest',
    license='MIT',
    author='Niel (Ketov) Gorev',
    author_email='ketov-x@yandex.ru',
    description='Bitrix24 REST API wrapper provides easy way to communicate with bitrix24 portal over REST without OAuth',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='bitrix24 async api rest',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Production/Stable',

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
