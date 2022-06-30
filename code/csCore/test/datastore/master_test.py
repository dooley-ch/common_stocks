# *******************************************************************************************
#  File:  master_test.py
#
#  Created: 30-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  30-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

import csCore.datastore as ds
import csCore.model.data as model


class TestMaster:
    def test_insert(self, mongodb_connection, database_name) -> None:
        store = ds.MasterStore(mongodb_connection, database_name)
        store.clear()

        record = model.MasterExt('IBM', 'IBM Corp', cik='3456', figi='345678', sub_industry='Technology')
        record.indexes.append(model.IndexName.SP100)
        record.indexes.append(model.IndexName.SP400)

        assert store.insert(record)

    def test_get(self, mongodb_connection, database_name) -> None:
        store = ds.MasterStore(mongodb_connection, database_name)
        store.clear()

        store = ds.MasterStore(mongodb_connection, database_name)
        store.clear()

        record = model.MasterExt('IBM', 'IBM Corp', cik='3456', figi='345678', sub_industry='Technology')
        record.indexes.append(model.IndexName.SP100)
        record.indexes.append(model.IndexName.SP400)

        assert store.insert(record)

        record = store.get('IBM')
        assert record
