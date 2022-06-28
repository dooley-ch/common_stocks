# *******************************************************************************************
#  File:  master_test.py
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

_master_data_1 = """
    {
        "ticker":"IBM",
        "name":"IBM Corp.",
        "cik":"3456",
        "figi":"345",
        "sub_industry":"Energy",
        "indexes":["sp100", "sp400"]
    }
"""

_master_data_2 = """
    {
        "ticker":"IBM",
        "name":"IBM Corp.",
        "cik":"3456",
        "figi":"345",
        "sub_industry":"Energy",
        "indexes":["sp100", "sp400"],
        "metadata": {
            "lock_version": 1,
            "created_at": "2022-06-16T16:28:29.940+00:00",
            "updated_at": "2022-06-16T16:28:29.940+00:00"
        }        
    }
"""


class TestMaster:
    """
    This class tests the Master DTO class
    """

    def test_create_minimum(self) -> None:
        record = db_model.Master('IBM', 'IBM Corp')
        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp'
        assert record.cik == '0000000000'
        assert record.figi == '000000000000'
        assert record.sub_industry == 'Unknown'

    def test_create(self) -> None:
        record = db_model.Master('IBM', 'IBM Corp', cik='3456', figi='345678', sub_industry='Technology')
        record.indexes.append(db_model.IndexName.SP100)
        record.indexes.append(db_model.IndexName.SP400)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp'
        assert record.cik == '0000003456'
        assert record.figi == '000000345678'
        assert record.sub_industry == 'Technology'
        assert len(record.indexes) == 2

    def test_create_ext(self) -> None:
        record = db_model.MasterExt('IBM', 'IBM Corp', cik='3456', figi='345678', sub_industry='Technology')
        record.indexes.append(db_model.IndexName.SP100)
        record.indexes.append(db_model.IndexName.SP400)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp'
        assert record.cik == '0000003456'
        assert record.figi == '000000345678'
        assert record.sub_industry == 'Technology'
        assert len(record.indexes) == 2
        assert record.metadata.lock_version == 1

    def test_parse(self) -> None:
        data = orjson.loads(_master_data_1)
        record = db_model.Master.parse(data)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert len(record.indexes) == 2

    def test_parse_ext(self) -> None:
        data = orjson.loads(_master_data_2)
        record = db_model.MasterExt.parse(data)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert len(record.indexes) == 2
        assert record.metadata.lock_version == 1
