# *******************************************************************************************
#  File:  _master.py
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
__all__ = ['Master', 'MasterList', 'MasterExt', 'MasterExtList']

from typing import NewType, Any
import attrs
from ._core import Metadata, IndexName


@attrs.frozen
class Master:
    ticker: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    cik: str = attrs.field(default='0000000000', converter=lambda value : value.zfill(10))
    figi: str = attrs.field(default='000000000000', converter=lambda value : value.zfill(12))
    sub_industry: str = attrs.field(default='Unknown', validator=[attrs.validators.instance_of(str)])
    indexes: list[IndexName] = attrs.Factory(list)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> Master:
        ticker = data['ticker']
        name = data['name']
        cik = data['cik']
        figi = data['figi']
        sub_ind = data['sub_industry']
        indexes = data['indexes']

        record = Master(ticker, name, cik, figi, sub_ind)

        for index in indexes:
            record.indexes.append(IndexName(index))

        return record

MasterList = NewType('MasterList', list[Master])


@attrs.frozen
class MasterExt(Master):
    metadata: Metadata = attrs.Factory(Metadata)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> MasterExt:
        ticker = data['ticker']
        name = data['name']
        cik = data['cik']
        figi = data['figi']
        sub_ind = data['sub_industry']
        indexes = data['indexes']
        metadata = data['metadata']

        record = MasterExt(ticker, name, cik=cik, figi=figi, sub_industry=sub_ind,  metadata =Metadata(**metadata))

        for index in indexes:
            record.indexes.append(IndexName(index))

        return record


MasterExtList = NewType('MasterExtList', list[MasterExt])
