# *******************************************************************************************
#  File:  _core.py
#
#  Created: 20-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  20-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['Metadata', 'IndexName']

from enum import Enum
from datetime import datetime
import attrs
import pendulum


class IndexName(str, Enum):
    SP100 = 'sp100'
    SP600 = 'sp600'
    SP400 = 'sp400'
    SP500 = 'sp500'


def _parse_metadata_date(value) -> datetime:
    """
    This function converts a datetime string to an instance of the datetime class
    """
    if isinstance(value, str):
        return pendulum.parse(value, strict=False)
    return value

@attrs.define
class Metadata:
    lock_version: int = attrs.field(default=0, converter=int)
    created_at: datetime = attrs.field(factory=datetime.now, converter=_parse_metadata_date)
    updated_at: datetime = attrs.field(factory=datetime.now, converter=_parse_metadata_date)
