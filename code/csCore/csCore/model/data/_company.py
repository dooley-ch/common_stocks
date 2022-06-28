# *******************************************************************************************
#  File:  _company.py
#
#  Created: 21-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  21-06-2022: Initial version
#
# *******************************************************************************************
from __future__ import annotations

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['Company', 'CompanyList', 'CompanyExt', 'CompanyExtList']

from typing import NewType, Any
import attrs
from ._core import Metadata, IndexName


@attrs.frozen
class Company:
    ticker: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    description: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    cik: str = attrs.field(default='0000000000', converter=lambda value: value.zfill(10),
                           validator=[attrs.validators.instance_of(str)])
    figi: str = attrs.field(default='000000000000', converter=lambda value: value.zfill(12),
                            validator=[attrs.validators.instance_of(str)])
    exchange: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    currency: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    country: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    sub_industry: str = attrs.field(default='Unknown', validator=[attrs.validators.instance_of(str)])
    indexes: list[IndexName] = attrs.Factory(list)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> Company:
        ticker = data['ticker']
        name = data['name']
        description = data['description']
        cik = data['cik']
        figi = data['figi']
        exchange = data['exchange']
        currency = data['currency']
        country = data['country']
        sub_industry = data['sub_industry']
        indexes = data['indexes']

        record = Company(ticker, name, description, cik, figi, exchange, currency, country, sub_industry)

        for index in indexes:
            record.indexes.append(IndexName(index))

        return record


CompanyList = NewType('CompanyList', list[Company])


@attrs.frozen
class CompanyExt(Company):
    metadata: Metadata = attrs.Factory(Metadata)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> CompanyExt:
        ticker = data['ticker']
        name = data['name']
        description = data['description']
        cik = data['cik']
        figi = data['figi']
        exchange = data['exchange']
        currency = data['currency']
        country = data['country']
        sub_industry = data['sub_industry']
        indexes = data['indexes']
        metadata = data['metadata']

        record = CompanyExt(ticker, name, description, cik, figi, exchange, currency, country, sub_industry,
                         metadata=Metadata(**metadata))

        for index in indexes:
            record.indexes.append(IndexName(index))

        return record


CompanyExtList = NewType('MasterExtList', list[Company])
