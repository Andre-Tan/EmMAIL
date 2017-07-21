from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name="emmail",
        version="0.5",
        description="EMM Automatic Isolate Labeler",
        long_description=long_description,
        url="https://github.com/Andre-Tan/EmMAIL",
        author="Andre Tan",
        author_email="andre.sutanto.91@gmail.com",
        license="GPL-3.0",
        packages=["emmail"],
        zip_safe=False,
        # install_requires=["biopython"],
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