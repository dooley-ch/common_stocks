# *******************************************************************************************
#  File:  config_test.py
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

import orjson
import csCore.model.data as db_model

_config_data_1 = """
    {
        "name":"database", 
        "items": [
            {"key": "user", "value": "tom_in_tears"}
        ]
    }
"""

_config_data_2 = """
    {
        "name":"database", 
        "items": [
            {"key": "user", "value": "tom_in_tears"}
        ],
        "metadata": {
            "lock_version": 1,
            "created_at": "2022-06-16T16:28:29.940+00:00",
            "updated_at": "2022-06-16T16:28:29.940+00:00"
        }
    }
"""


class TestConfig:
    """
    This class tests the Config DTO class
    """
    def test_create(self) -> None:
        cfg = db_model.Config('database')
        assert cfg.name == 'database'
        assert len(cfg.items) == 0

    def test_create_item(self) -> None:
        cfg_item = db_model.ConfigItem('user', 'tom_in_tears')
        assert cfg_item.key == 'user'
        assert cfg_item.value == 'tom_in_tears'

        cfg = db_model.Config('database')
        cfg.items.append(cfg_item)

        assert cfg.name == 'database'
        assert len(cfg.items) == 1

    def test_create_extended(self) -> None:
        cfg = db_model.ConfigExt('database')
        assert cfg.name == 'database'
        assert len(cfg.items) == 0
        assert cfg.metadata.lock_version == 1

    def test_parse_config(self) -> None:
        data = orjson.loads(_config_data_1)
        cfg = db_model.Config.parse(data)

        assert cfg.name == 'database'
        assert len(cfg.items) == 1

        item = cfg.items[0]
        assert isinstance(item, db_model.ConfigItem)

        assert item.key == 'user'
        assert item.value == 'tom_in_tears'

    def test_parse_config_ext(self) -> None:
        data = orjson.loads(_config_data_2)
        cfg = db_model.ConfigExt.parse(data)

        assert cfg.name == 'database'
        assert len(cfg.items) == 1

        item = cfg.items[0]
        assert isinstance(item, db_model.ConfigItem)

        assert item.key == 'user'
        assert item.value == 'tom_in_tears'
