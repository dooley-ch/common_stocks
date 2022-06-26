# *******************************************************************************************
#  File:  _edgar_sec.py
#
#  Created: 25-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  25-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['EdgarSecService']

import orjson
import csCore.model.service as model
from ._core import get_page


class EdgarSecService:
    _url: str

    def __init__(self, url: str) -> object:
        self._url = url

    def get_codes(self) -> model.CikCodeList | None:
        contents = get_page(self._url)

        if contents:
            data = orjson.loads(contents)
            fields = data['fields']
            rows = data['data']

            records: model.CikCodeList = list()

            for row in rows:
                record_data = dict(zip(fields, row))
                record = model.CikCode.parse(record_data)
                records.append(record)

            return records
