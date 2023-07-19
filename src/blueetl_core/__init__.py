"""BlueETL core transformations."""
from blueetl_core.etl import register_accessors
from blueetl_core.version import __version__  # noqa

# registration of Pandas accessors
register_accessors()
