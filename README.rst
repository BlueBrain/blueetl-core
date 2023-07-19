blueetl-core
============

Core transformations for BlueETL


Introduction
------------

``BlueETL-core`` automatically registers Pandas accessors using the ``.etl`` namespace, that can be useful to simplify some recurring operations on Pandas DataFrames, Series, and Indexes.

It provides the core transformations used by `BlueETL <https://bbpteam.epfl.ch/documentation/projects/blueetl/latest/index.html>`__, a package that can help analyse multiple simulations in a Simulation Campaign.


Installation
------------

``BlueETL-core`` can be installed independently from ``BlueETL`` with::

    PIP_INDEX_URL=https://bbpteam.epfl.ch/repository/devpi/simple \
    pip install -U blueetl-core


Usage
-----

To use the Core Transformations provided by the ``.etl`` accessor with any Pandas DataFrame or Series, it's enough to import BlueETL or BlueETL-core, and call the desired methods.

For example:

.. code-block:: python


    import blueetl_core
    import pandas as pd

    df = pd.DataFrame({"a": [0, 1, 2], "b": [3, 4, 5]})
    df = df.etl.q(a=1)

See `this Jupyter notebook <https://bbpteam.epfl.ch/documentation/projects/blueetl/latest/notebooks/01_core_transformations.html>`__ for more information and examples.


Reporting issues
----------------

``BlueETL-core`` is maintained by the BlueBrain NSE team.

Should you face any issue with using it, please submit a ticket to our `issue tracker <https://bbpteam.epfl.ch/project/issues/browse/NSETM>`__.
