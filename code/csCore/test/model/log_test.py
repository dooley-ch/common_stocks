# *******************************************************************************************
#  File:  log_test.py
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

import orjson
import csCore.model.data as db_model

_data = """
    {
        "message":"Test Message",
        "level":"ERROR",
        "logged_at": "2022-06-16T16:28:29.940+00:00",
        "function": "",
        "file": "",
        "line":0
    }
"""


class TestLog:
    def test_create(self) -> None:
        record = db_model.CSApiLog('Test Message')

        assert record.message == 'Test Message'
        assert record.level == db_model.LogLevel.error

    def test_parse(self) -> None:
        data = orjson.loads(_data)
        record = db_model.CSApiActivityLog.parse(data)

        assert isinstance(record, db_model.CSApiActivityLog)
