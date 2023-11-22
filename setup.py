#!/usr/bin/env python
import importlib.util
from pathlib import Path

from setuptools import find_namespace_packages, setup

spec = importlib.util.spec_from_file_location(
    "blueetl_core.version",
    "src/blueetl_core/version.py",
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
VERSION = module.__version__

setup(
    name="blueetl-core",
    author="bbp-ou-nse",
    author_email="bbp-ou-nse@groupes.epfl.ch",
    version=VERSION,
    description="Core transformations for BlueETL",
    long_description=Path("README.rst").read_text(encoding="utf-8"),
    long_description_content_type="text/x-rst",
    url="https://bbpteam.epfl.ch/documentation/projects/blueetl-core",
    project_urls={
        "Tracker": "https://bbpteam.epfl.ch/project/issues/projects/NSETM/issues",
        "Source": "https://github.com/BlueBrain/blueetl-core.git",
    },
    license="BBP-internal-confidential",
    install_requires=[
        "numpy>=1.19.4",
        "pandas>=1.3.0",
        "joblib>=1.3.1",
        "packaging>=21.3",
    ],
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.9",
    extras_require={"docs": ["sphinx", "sphinx-bluebrain-theme"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
