# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBlueetlCore(PythonPackage):
    """Core transformations for BlueETL"""

    homepage = "https://bbpteam.epfl.ch/documentation/projects/blueetl-core"
    git = "git@bbpgitlab.epfl.ch:nse/blueetl-core.git"

    version("develop", branch="main")
    version("0.1.0.dev0", tag="blueetl-core-v0.1.0.dev0")

    depends_on("py-setuptools", type="build")  # type=("build", "run") if specifying entry points in 'setup.py'

    # for all 'foo>=X' in 'install_requires' and 'extra_requires':
    # depends_on("py-foo@<min>:", type=("build", "run"))

    # for any C/C++ build dependencies and/or CMake:
    # depends_on("cmake", type="build")
    # depends_on("boost")
