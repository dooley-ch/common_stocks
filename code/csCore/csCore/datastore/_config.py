# *******************************************************************************************
#  File:  _config.py
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
__all__ = ['ConfigStore']

from attrs import asdict
from pymongo.results import UpdateResult
import csCore.model.data as model
from ._core import CollectionBase


class ConfigStore(CollectionBase):
    """
    This class provides access to the config collection
    """
    def __init__(self, url: str, database_name: str) -> object:
        super().__init__(url, database_name, 'config')

    def get(self, name: str) -> model.ConfigExt | None:
        raw_data = self._collection.find_one({'name': name}, {'_id': 0})
        if raw_data:
            return model.ConfigExt.parse(raw_data)

    def insert(self, record: model.ConfigExt) -> bool:
        return self._insert(record)

    def update(self, record: model.ConfigExt) -> bool:
        values = list()
        for item in record.items:
            data = asdict(item)
            values.append(data)

        record.metadata.update()

        result: UpdateResult = self._collection.update_one({'name': record.name},
                                                           {'$set':
                                                                {'items': values, 'metadata': asdict(record.metadata)}})

        return result.acknowledged
