Changelog
=========

Version 0.2.1
-------------

New Features
~~~~~~~~~~~~

- Add ``blueetl_core.parallel.isolated()`` to execute a function in a separate subprocess.

Improvements
~~~~~~~~~~~~

- If the env variable ``BLUEETL_SUBPROCESS_LOGGING_LEVEL`` is empty or not defined, then the log level of the subprocesses is inherited from the parent.

Version 0.2.0
-------------

New Features
~~~~~~~~~~~~

- Add ``df.etl.insert_columns()`` to simplify the insertion of multiple columns at once in a DataFrame.

Improvements
~~~~~~~~~~~~

- In ``run_parallel()``, automatically shutdown the processes created by joblib and loky.


Version 0.1.8
-------------

Improvements
~~~~~~~~~~~~

- Update github actions.
- Split lint and docs jobs in the CI.
- Remove tox-gh-actions in the CI.
- Use tox-uv in the CI.
- Update black formatting.

Version 0.1.7
-------------

Improvements
~~~~~~~~~~~~

- Technical update: Update badges.

Version 0.1.6
-------------

Improvements
~~~~~~~~~~~~

- Technical update: Use PYPI_API_TOKEN instead of PYPI_PASSWORD.

Version 0.1.5
-------------

Improvements
~~~~~~~~~~~~

- Technical update: Fix banner and license.

Version 0.1.4
-------------

Improvements
~~~~~~~~~~~~

- Technical update: OSS release.

Version 0.1.3
-------------

Bug fixes
~~~~~~~~~

- Ignore ``skip_empty`` in ``utils.smart_concat()`` when all the DataFrames are empty.

Version 0.1.2
-------------

Improvements
~~~~~~~~~~~~

- Use ``skip_empty=True`` by default in ``utils.smart_concat()``.

Version 0.1.1
-------------

Improvements
~~~~~~~~~~~~

- Update documentation.

Version 0.1.0
-------------

New Features
~~~~~~~~~~~~

- First release, split from BlueETL 0.3.0.dev3.
