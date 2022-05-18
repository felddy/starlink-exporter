"""
This is the setup module for the starlink-exporter docker project.

Based on:

- https://packaging.python.org/distributing/
- https://github.com/pypa/sampleproject/blob/master/setup.py
- https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
"""

# Standard Python Libraries
from glob import glob
from os.path import basename, splitext

# Third-Party Libraries
from setuptools import find_packages, setup


def readme():
    """Read in and return the contents of the project's README.md file."""
    with open("README.md", encoding="utf-8") as f:
        return f.read()


def package_vars(version_file):
    """Read in and return the variables defined by the version_file."""
    pkg_vars = {}
    with open(version_file) as f:
        exec(f.read(), pkg_vars)  # nosec
    return pkg_vars


setup(
    name="starlink_exporter",
    # Versions should comply with PEP440
    version=package_vars("src/_version.py")["__version__"],
    description="starlink_exporter python library",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/felddy",
    # The project's main homepage
    download_url="https://github.com/felddy/starlink-exporter",
    # Author details
    author="Mark Feldhousen",
    author_email="markf@geekpad.com",
    license="License :: OSI Approved :: MIT License",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: System :: Networking :: Monitoring",
    ],
    python_requires=">=3.6",
    # What does your project relate to?
    keywords="starlink prometheus",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    install_requires=[
        "docopt",
        "grpcio == 1.46.1",
        "grpcio-tools == 1.46.1",
        "schema",
        "setuptools >= 24.2.0",
    ],
    extras_require={
        "test": [
            "coverage",
            # coveralls 1.11.0 added a service number for calls from
            # GitHub Actions. This caused a regression which resulted in a 422
            # response from the coveralls API with the message:
            # Unprocessable Entity for url: https://coveralls.io/api/v1/jobs
            # 1.11.1 fixed this issue, but to ensure expected behavior we'll pin
            # to never grab the regression version.
            "coveralls != 1.11.0",
            "pre-commit",
            "pytest-cov",
            "pytest",
        ]
    },
    # Conveniently allows one to run the CLI tool as `example`
    entry_points={
        "console_scripts": [
            "starlink-exporter = starlink_exporter.starlink_exporter:main"
        ]
    },
)
