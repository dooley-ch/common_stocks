# *******************************************************************************************
#  File:  _master.py
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
__all__ = ['MasterStore']

import csCore.model.data as model
from ._core import CollectionBase


class MasterStore(CollectionBase):
    """
    This class provides access to the master table
    """
    def __init__(self, url: str, database_name: str) -> object:
        super().__init__(url, database_name, 'master')

    def get(self, ticker: str) -> model.Master:
        pass

    def insert(self, record: model.MasterExt) -> bool:
        return self._insert(record)
