# *******************************************************************************************
#  File:  _earnings.py
#
#  Created: 22-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  22-06-2022: Initial version
#
# *******************************************************************************************
from __future__ import annotations

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['AnnualEarnings', 'QuarterEarnings', 'Earnings', 'EarningsExt']

from datetime import datetime
from typing import Any
import attrs
from ._core import Metadata, parse_record_date


@attrs.frozen
class AnnualEarnings:
    year_end: datetime = attrs.field(validator=[attrs.validators.instance_of(datetime)], converter=parse_record_date)
    earnings: str = attrs.field(validator=[attrs.validators.instance_of(str)])


@attrs.frozen
class QuarterEarnings:
    quarter_end: datetime = attrs.field(validator=[attrs.validators.instance_of(datetime)], converter=parse_record_date)
    reported: datetime = attrs.field(validator=[attrs.validators.instance_of(datetime)], converter=parse_record_date)
    earnings: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    estimate: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    surprise: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    surprise_percent: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])


@attrs.frozen
class Earnings:
    ticker: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    annual: list[AnnualEarnings] = attrs.Factory(list)
    quarter: list[QuarterEarnings] = attrs.Factory(list)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> Earnings:
        ticker = data['ticker']
        name = data['name']
        annual = data['annual']
        quarter = data['quarter']

        record = Earnings(ticker, name)

        for item in annual:
            record.annual.append(AnnualEarnings(**item))

        for item in quarter:
            record.quarter.append(QuarterEarnings(**item))

        return record


@attrs.frozen
class EarningsExt(Earnings):
    metadata: Metadata = attrs.Factory(Metadata)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> EarningsExt:
        ticker = data['ticker']
        name = data['name']
        annual = data['annual']
        quarter = data['quarter']
        metadata = data['metadata']

        record = EarningsExt(ticker, name, metadata=Metadata(**metadata))

        for item in annual:
            record.annual.append(AnnualEarnings(**item))

        for item in quarter:
            record.quarter.append(QuarterEarnings(**item))

        return record
