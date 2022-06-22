# *******************************************************************************************
#  File:  earnings_test.py
#
#  Created: 22-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  22-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

import datetime
import orjson
import csCore.model.data as db_model

_data_1 = """
    {
        "ticker":"IBM",
        "name":"IBM Corp.",
        "annual":[
            {"year_end":"2022-06-16T16:28:29.940+00:00", "earnings":"34.5"},
            {"year_end":"2021-06-16T16:28:29.940+00:00", "earnings":"31.5"}
        ],
        "quarter":[
            {
                "quarter_end":"2022-06-16T16:28:29.940+00:00",
                "reported":"2022-06-16T16:28:29.940+00:00",
                "earnings":"34.5",
                "estimate":"",
                "surprise":"",
                "surprise_percent":""
            }
        ]
    }
"""

_data_2 = """
    {
        "ticker":"IBM",
        "name":"IBM Corp.",
        "annual":[
            {"year_end":"2022-06-16T16:28:29.940+00:00", "earnings":"34.5"},
            {"year_end":"2021-06-16T16:28:29.940+00:00", "earnings":"31.5"}
        ],
        "quarter":[
            {
                "quarter_end":"2022-06-16T16:28:29.940+00:00",
                "reported":"2022-06-16T16:28:29.940+00:00",
                "earnings":"34.5",
                "estimate":"",
                "surprise":"",
                "surprise_percent":""
            }
        ],
        "metadata": {
            "lock_version": 1,
            "created_at": "2022-06-16T16:28:29.940+00:00",
            "updated_at": "2022-06-16T16:28:29.940+00:00"
        }
    }
"""


class TestEarnings:
    """
    This class tests the Earnings DTO class
    """
    def test_create_minimum(self) -> None:
        record = db_model.Earnings('IBM', 'IBM Corp.')

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'

    def test_create(self) -> None:
        record = db_model.Earnings('IBM', 'IBM Corp.')
        record.annual.append(db_model.AnnualEarnings(datetime.datetime(2020, 12, 31), '23.33'))
        record.annual.append(db_model.AnnualEarnings(datetime.datetime(2021, 12, 31), '23.33'))
        record.quarter.append(db_model.QuarterEarnings(datetime.datetime(2020, 12, 31),
                                                       datetime.datetime(2020, 12, 31), '23.33'))
        record.quarter.append(db_model.QuarterEarnings(datetime.datetime(2021, 12, 31),
                                                       datetime.datetime(2020, 12, 31), '23.33'))

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert len(record.annual) == 2
        assert len(record.quarter)  == 2

    def test_create_extended(self) -> None:
        record = db_model.EarningsExt('IBM', 'IBM Corp.')

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'

    def test_parse_earnings(self) -> None:
        data = orjson.loads(_data_1)
        record = db_model.Earnings.parse(data)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert len(record.annual) == 2
        assert len(record.quarter)  == 1

    def test_parse_earnings_ext(self) -> None:
        data = orjson.loads(_data_2)
        record = db_model.EarningsExt.parse(data)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert len(record.annual) == 2
        assert len(record.quarter)  == 1
        assert record.metadata.lock_version == 1
