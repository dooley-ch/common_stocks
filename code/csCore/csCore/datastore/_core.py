# *******************************************************************************************
#  File:  _core.py
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
__all__ = ['DatastoreBase', 'CollectionBase']

from attrs import asdict
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.results import InsertManyResult
from pymongo.errors import DuplicateKeyError
from typing import Any
from csCore.errors import DuplicateKeyError


class DatastoreBase:
    """
    Base class used to access the database
    """
    _database: Database

    def __init__(self, url: str, database_name: str) -> object:
        client = MongoClient(url)
        self._database = client[database_name]


class CollectionBase(DatastoreBase):
    """
    Base class used to work with a collection
    """
    _collection: Collection

    def __init__(self, url: str, database_name: str, collection_name: str) -> object:
        super().__init__(url, database_name)
        self._collection = self._database[collection_name]

    def _insert(self, record: Any) -> bool:
        """
        This method inserts a record in the collection
        :param record: The record to insert
        :return: True if successful otherwise False
        """
        try:
            results: InsertManyResult = self._collection.insert_one(asdict(record))
        except DuplicateKeyError as e:
            raise DuplicateKeyError(record, str(e))
        else:
            return results.acknowledged

    def clear(self) -> None:
        """
        This method deletes all the records in the database
        """
        self._collection.delete_many({})
