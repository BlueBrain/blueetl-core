"""BlueETL core transformations."""

from blueetl_core._version import __version__  # noqa
from blueetl_core.etl import register_accessors

# registration of Pandas accessors
register_accessors()
