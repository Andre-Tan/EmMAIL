from sys import exit, version_info
from os import environ
import logging

logging.basicConfig(level=environ.get("LOGLEVEL", "INFO"))

if version_info <= (3, 0):
    logging.fatal("Sorry, requires Python 3.x, not Python 2.x\n")
    exit(1)

from setuptools import setup
import emmail

with open("README.md", "r") as f:
    long_description = f.read()

setup(name= emmail.__name__,
        version = emmail.__version__,
        description = emmail.__description__,
        long_description=long_description,
        url = emmail.__url__,
        author = emmail.__author__,
        author_email= emmail.__email__,
        license = emmail.__license__,
        packages=["emmail"],
        zip_safe=False,
        install_requires = [
            "scipy>=1", 
            "numpy>=1"],
        test_suite="nose.collector",
        tests_require=["nose"],
        scripts=["bin/emmail"],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Scientific/Engineering :: Bio-Informatics"
        ]
    )