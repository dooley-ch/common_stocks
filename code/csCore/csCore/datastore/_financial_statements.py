# *******************************************************************************************
#  File:  _financial_statements.py
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
__all__ = ['FinancialStatementsStore']

import csCore.model.data as model
from ._core import CollectionBase


class FinancialStatementsStore(CollectionBase):
    """
    This class provides access to the financial statements collection
    """
    def __init__(self, url: str, database_name: str) -> object:
        super().__init__(url, database_name, 'financial_statements')

    def get(self, ticker: str) -> model.FinancialStatements:
        raw_data = self._collection.find_one({'ticker': ticker}, {'_id': 0})
        if raw_data:
            return model.FinancialStatementsExt.parse(raw_data)

    def insert(self, record: model.FinancialStatementsExt) -> bool:
        return self._insert(record)
