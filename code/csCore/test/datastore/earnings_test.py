# *******************************************************************************************
#  File:  earnings_test.py
#
#  Created: 28-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  28-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

from datetime import datetime
import csCore.datastore as ds
import csCore.model.data as model


class TestEarnings:
    def test_insert(self, mongodb_connection, database_name) -> None:
        store = ds.EarningsStore(mongodb_connection, database_name)
        store.clear()

        record = model.EarningsExt('IBM', 'IBM Corp.')
        record.annual.append(model.AnnualEarnings(datetime(2020, 12, 31), '23.33'))
        record.annual.append(model.AnnualEarnings(datetime(2021, 12, 31), '23.33'))
        record.quarter.append(model.QuarterEarnings(datetime(2020, 12, 31),
                                                       datetime(2020, 12, 31), '23.33'))
        record.quarter.append(model.QuarterEarnings(datetime(2021, 12, 31),
                                                       datetime(2020, 12, 31), '23.33'))

        assert store.insert(record)

    def test_get(self, mongodb_connection, database_name) -> None:
        store = ds.EarningsStore(mongodb_connection, database_name)
        store.clear()

        record = model.EarningsExt('IBM', 'IBM Corp.')
        record.annual.append(model.AnnualEarnings(datetime(2020, 12, 31), '23.33'))
        record.annual.append(model.AnnualEarnings(datetime(2021, 12, 31), '23.33'))
        record.quarter.append(model.QuarterEarnings(datetime(2020, 12, 31),
                                                       datetime(2020, 12, 31), '23.33'))
        record.quarter.append(model.QuarterEarnings(datetime(2021, 12, 31),
                                                       datetime(2020, 12, 31), '23.33'))

        assert store.insert(record)

        record = store.get('IBM')
        assert record.name == 'IBM Corp.'
        assert len(record.annual) == 2
        assert len(record.quarter) == 2

    def test_clear(self, mongodb_connection, database_name) -> None:
        store = ds.EarningsStore(mongodb_connection, database_name)
        store.clear()

        record = model.EarningsExt('IBM', 'IBM Corp.')
        record.annual.append(model.AnnualEarnings(datetime(2020, 12, 31), '23.33'))
        record.annual.append(model.AnnualEarnings(datetime(2021, 12, 31), '23.33'))
        record.quarter.append(model.QuarterEarnings(datetime(2020, 12, 31),
                                                       datetime(2020, 12, 31), '23.33'))
        record.quarter.append(model.QuarterEarnings(datetime(2021, 12, 31),
                                                       datetime(2020, 12, 31), '23.33'))

        assert store.insert(record)

        record = store.get('IBM')
        assert record

        store.clear()
        record = store.get('IBM')
        assert record is None
