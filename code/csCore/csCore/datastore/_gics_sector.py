# *******************************************************************************************
#  File:  _gics_sector.py
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
__all__ = ['GicsSectorStore']

import csCore.model.data as model
from ._core import CollectionBase


class GicsSectorStore(CollectionBase):
    """
    Provides access to the gics sector collection
    """
    def __init__(self, url: str, database_name: str) -> object:
        super().__init__(url, database_name, 'gics_sector')

    def get(self, name: str) -> model.GicsSectorExt:
        raw_data = self._collection.find_one({'name': name}, {'_id': 0})
        if raw_data:
            return model.GicsSectorExt.parse(raw_data)

    def insert(self, record: model.GicsSectorExt) -> bool:
        return self._insert(record)
