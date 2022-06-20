# *******************************************************************************************
#  File:  _config.py
#
#  Created: 20-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  20-06-2022: Initial version
#
# *******************************************************************************************
from __future__ import annotations

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['ConfigItem', 'Config', 'ConfigList', 'ConfigExt', 'ConfigExtList']


from typing import NewType, Any
import attrs
from ._core import Metadata


@attrs.frozen
class ConfigItem:
    """
    This class represents a configuration value defined in a configuration record
    """
    key: str
    value: str


ConfigItemList = NewType('ConfigItemList', list[ConfigItem])


@attrs.frozen
class Config:
    """
    This class represents a business content of a record stored in the database
    """
    name: str
    items: ConfigItemList = attrs.Factory(list)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> Config:
        name = data['name']
        items = data['items']

        record = Config(name)

        for item in items:
            record.items.append(ConfigItem(**item))

        return record


@attrs.frozen
class ConfigExt(Config):
    """
    This class represents a  record stored in the database
    """
    metadata: Metadata = attrs.Factory(Metadata)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> Config:
        name = data['name']
        items = data['items']
        meta_data = data['metadata']

        record = ConfigExt(name, metadata=Metadata(**meta_data))

        for item in items:
            record.items.append(ConfigItem(**item))

        return record


ConfigList = NewType('ConfigList', list[Config])
ConfigExtList = NewType('ConfigExtList', list[ConfigExt])
