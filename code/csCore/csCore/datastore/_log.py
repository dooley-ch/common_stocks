# *******************************************************************************************
#  File:  _log_file.py
#
#  Created: 27-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  27-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['LogFile']

from typing import TypeVar, Generic

from ._core import CollectionBase

T = TypeVar('T')


class LogFile(CollectionBase, Generic[T]):
    def insert(self, record: T) -> bool:
        return self._insert(record)
