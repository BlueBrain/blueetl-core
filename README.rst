|banner|

|build_status| |license| |coverage| |docs| |CodeQL| |PyPI| |DOI|

blueetl-core
============

Core transformations for BlueETL.


Introduction
------------

``BlueETL-core`` automatically registers Pandas accessors using the ``.etl`` namespace, that can be useful to simplify some recurring operations on Pandas DataFrames, Series, and Indexes.

It provides the core transformations used by `BlueETL <https://github.com/BlueBrain/blueetl>`__, a package that can help analyse multiple simulations in a Simulation Campaign.


Installation
------------

``BlueETL-core`` can be installed independently from ``BlueETL`` with::

    pip install -U blueetl-core


Examples
--------

To use the Core Transformations provided by the ``.etl`` accessor with any Pandas DataFrame or Series, it's enough to import BlueETL or BlueETL-core, and call the desired methods.

For example:

.. code-block:: python


    import blueetl_core
    import pandas as pd

    df = pd.DataFrame({"a": [0, 1, 2], "b": [3, 4, 5]})
    df = df.etl.q(a=1)

See `this Jupyter notebook <https://blueetl.readthedocs.io/en/stable/notebooks/01_core_transformations.html>`__ for more information and examples.


Contribution Guidelines
-----------------------

See `<CONTRIBUTING.rst>`__.


Citation
--------

When you use this software, we kindly ask you to cite the following DOI:

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.10277477.svg
   :target: https://doi.org/10.5281/zenodo.10277477


Acknowledgment
--------------

The development of this software was supported by funding to the Blue Brain Project, a research center of the École polytechnique fédérale de Lausanne (EPFL), from the Swiss government’s ETH Board of the Swiss Federal Institutes of Technology.

For license and authors, see `<LICENSE.txt>`__ and `<AUTHORS.txt>`__ respectively.

Copyright © 2023 Blue Brain Project/EPFL


.. |build_status| image:: https://github.com/BlueBrain/blueetl-core/actions/workflows/run-tox.yml/badge.svg
   :alt: Build Status

.. |license| image:: https://img.shields.io/pypi/l/blueetl-core
   :target: https://github.com/BlueBrain/blueetl-core/blob/main/LICENSE.txt
   :alt: License

.. |coverage| image:: https://codecov.io/github/BlueBrain/blueetl-core/coverage.svg?branch=main
   :target: https://codecov.io/github/BlueBrain/blueetl-core?branch=main
   :alt: codecov.io

.. |docs| image:: https://readthedocs.org/projects/blueetl-core/badge/?version=latest
   :target: https://blueetl-core.readthedocs.io/
   :alt: documentation status

.. |CodeQL| image:: https://github.com/BlueBrain/blueetl-core/actions/workflows/github-code-scanning/codeql/badge.svg
   :target: https://github.com/BlueBrain/blueetl-core/actions/workflows/github-code-scanning/codeql
   :alt: CodeQL

.. |PyPI| image:: https://github.com/BlueBrain/blueetl-core/actions/workflows/publish-sdist.yml/badge.svg
   :target: https://pypi.org/project/blueetl-core/
   :alt: PyPI

.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.10277477.svg
   :target: https://doi.org/10.5281/zenodo.10277477
   :alt: DOI

.. local-substitutions

.. |banner| image:: https://raw.githubusercontent.com/BlueBrain/blueetl-core/main/doc/source/_images/BlueETL.jpeg
