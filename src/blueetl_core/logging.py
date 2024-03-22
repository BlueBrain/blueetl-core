"""BlueETL core transformations."""

import logging
from typing import Optional, Union

L = logging.getLogger(__name__)


def setup_logging(loglevel: Union[int, str], logformat: Optional[str] = None, **logparams) -> None:
    """Setup logging."""
    logformat = logformat or "%(asctime)s %(levelname)s %(name)s: %(message)s"
    logging.basicConfig(format=logformat, level=loglevel, **logparams)
