# *******************************************************************************************
#  File:  config_test.py
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


import csCore.datastore as ds
import csCore.model.data as model


class TestConfig:
    def test_insert(self, mongodb_connection, database_name) -> None:
        store = ds.ConfigStore(mongodb_connection, database_name)
        store.clear()

        item = model.ConfigItem('user', 'Tom234')
        cfg = model.ConfigExt('database')
        cfg.items.append(item)

        assert store.insert(cfg)

    def test_update(self, mongodb_connection, database_name) -> None:
        store = ds.ConfigStore(mongodb_connection, database_name)
        store.clear()

        item = model.ConfigItem('user', 'Tom234')
        cfg = model.ConfigExt('database')
        cfg.items.append(item)

        assert store.insert(cfg)

        record = store.get('database')
        assert record.name == 'database'
        assert len(record.items) == 1

        record.items[0].value = 'Mike'
        assert store.update(record)

        record = store.get('database')
        assert record.items[0].value == 'Mike'

    def test_get(self, mongodb_connection, database_name) -> None:
        store = ds.ConfigStore(mongodb_connection, database_name)
        store.clear()

        item = model.ConfigItem('user', 'Tom234')
        cfg = model.ConfigExt('database')
        cfg.items.append(item)

        assert store.insert(cfg)

        record = store.get('database')
        assert record.name == 'database'
        assert len(record.items) == 1

        item = record.items[0]
        assert item.key == 'user'
        assert item.value == 'Tom234'

    def test_all(self, mongodb_connection, database_name) -> None:
        store = ds.ConfigStore(mongodb_connection, database_name)
        store.clear()

        item = model.ConfigItem('user', 'Tom234')
        cfg = model.ConfigExt('database')
        cfg.items.append(item)
        assert store.insert(cfg)

        cfg = model.ConfigExt('webservice')
        cfg.items.append(item)
        assert store.insert(cfg)

        records = store.all()
        assert len(records) == 2
        assert 'database' in records
        assert 'webservice' in records

    def test_clear(self, mongodb_connection, database_name) -> None:
        store = ds.ConfigStore(mongodb_connection, database_name)
        store.clear()

        item = model.ConfigItem('user', 'Tom234')
        cfg = model.ConfigExt('database')
        cfg.items.append(item)

        assert store.insert(cfg)

        record = store.get('database')
        assert record

        store.clear()
        record = store.get('database')
        assert record is None
