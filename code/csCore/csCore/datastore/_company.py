# *******************************************************************************************
#  File:  _company.py
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
__all__ = ['CompanyStore']

import csCore.model.data as model
from ._core import CollectionBase


class CompanyStore(CollectionBase):
    """
    This class provides access to the company collection
    """
    def __init__(self, url: str, database_name: str) -> object:
        super().__init__(url, database_name, 'company')

    def get(self, ticker: str) -> model.CompanyExt:
        raw_data = self._collection.find_one({'ticker': ticker})
        if raw_data:
            return model.CompanyExt.parse(raw_data)

    def insert(self, record: model.CompanyExt) -> bool:
        return self._insert(record)
