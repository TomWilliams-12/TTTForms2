from .base import *
import os


if os.environ.get("RDS_DB_NAME") is None:
    from .local import *