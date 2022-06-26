# *******************************************************************************************
#  File:  service.py
#
#  Created: 24-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  24-06-2022: Initial version
#
# *******************************************************************************************
from __future__ import annotations

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['FigiCode', 'FigiCodeList', 'CikCode', 'CikCodeList', 'SpComponent', 'SpComponentList', 'AccountingItem',
           'AccountingItemList', 'AccountingItemDict', 'Statement', 'FinancialStatements', 'CompanyOverview',
           'EarningsCalendar', 'EarningsCalendarList']

from datetime import datetime
from typing import NewType, Any
import attrs
import pendulum


def parse_record_date(value) -> datetime:
    """
    This function converts a datetime string to an instance of the datetime class
    """
    if isinstance(value, str):
        return pendulum.parse(value, strict=False)
    return value


@attrs.frozen
class FigiCode:
    ticker: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    figi: str = attrs.field(converter=lambda value: value.zfill(12), validator=[attrs.validators.instance_of(str)])

    @classmethod
    def parse(cls, data: dict[str, Any]) -> FigiCode:
        return FigiCode(**data)


FigiCodeList = NewType('FigiCodeList', list[FigiCode])


@attrs.frozen
class CikCode:
    cik: str = attrs.field(converter=lambda value: str(value).zfill(10), validator=[attrs.validators.instance_of(str)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    ticker: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    exchange: str = attrs.field(validator=[attrs.validators.instance_of(str)])

    @classmethod
    def parse(cls, data: dict[str, Any]) -> CikCode:
        return CikCode(**data)


CikCodeList = NewType('CikCodeList', list[CikCode])


@attrs.frozen
class SpComponent:
    ticker: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    sector: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    sub_industry: str = attrs.field(validator=[attrs.validators.instance_of(str)])

    @classmethod
    def parse(cls, data: dict[str, Any]) -> SpComponent:
        return SpComponent(**data)


SpComponentList = NewType('SpComponentList', list[SpComponent])


@attrs.define
class AccountingItem:
    tag: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    value_1: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    value_2: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    value_3: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    value_4: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    value_5: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])

    @classmethod
    def parse(cls, data: dict[str, Any]) -> AccountingItem:
        return AccountingItem(**data)


AccountingItemList = NewType('AccountingItemList', list[AccountingItem])
AccountingItemDict = NewType('AccountingItemDict', dict[str, AccountingItem])


@attrs.frozen
class Statement:
    annual: AccountingItemDict = attrs.Factory(dict)
    quarter: AccountingItemDict = attrs.Factory(dict)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> Statement:
        annual = data['annual']
        quarter = data['quarter']

        record = Statement()

        for item in annual:
            acc_item = AccountingItem.parse(item)
            record.annual[acc_item.tag] = acc_item

        for item in quarter:
            acc_item = AccountingItem.parse(item)
            record.quarter[acc_item.tag] = acc_item

        return record


@attrs.frozen
class FinancialStatements:
    ticker: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    income: Statement = attrs.Factory(Statement)
    cash_flow: Statement = attrs.Factory(Statement)
    balance_sheet: Statement = attrs.Factory(Statement)
    earnings: Statement = attrs.Factory(Statement)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> FinancialStatements:
        ticker = data['ticker']
        name = data['name']
        income_data = data['income']
        cash_flow_data = data['cash_flow']
        balance_sheet_data = data['balance_sheet']
        earnings_data = data['earnings']

        income = Statement.parse(income_data)
        cash_flow = Statement.parse(cash_flow_data)
        balance_sheet = Statement.parse(balance_sheet_data)
        earnings_data = Statement.parse(earnings_data)

        record = FinancialStatements(ticker, name, income, cash_flow, balance_sheet, earnings_data)
        return record


@attrs.frozen
class CompanyOverview:
    ticker: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    description: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    cik: str = attrs.field(converter=lambda value: value.zfill(10), validator=[attrs.validators.instance_of(str)])
    exchange: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    currency: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    country: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    sector: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    industry: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    address: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    fiscal_year_end: str = attrs.field(validator=[attrs.validators.instance_of(str)])

    @classmethod
    def parse(cls, data: dict[str, Any]) -> CompanyOverview:
        ticker = data['Symbol']
        name = data['Name']
        description = data['Description']
        cik = data['CIK']
        exchange = data['Exchange']
        currency = data['Currency']
        country = data['Country']
        sector = data['Sector']
        industry = data['Industry']
        address = data['Address']
        fiscal_year_end = data['FiscalYearEnd']

        return CompanyOverview(ticker, name, description, cik, exchange, currency, country,
                               sector, industry, address, fiscal_year_end)


@attrs.frozen
class EarningsCalendar:
    ticker: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    report_date: datetime = attrs.field(factory=datetime, validator=[attrs.validators.instance_of(datetime)],
                                        converter=parse_record_date)
    fiscal_date_ending: datetime = attrs.field(factory=datetime, validator=[attrs.validators.instance_of(datetime)],
                                               converter=parse_record_date)
    estimate: int = attrs.field(default=0, validator=[attrs.validators.instance_of(int)], converter=int)
    currency: str = attrs.field(default='USD', validator=[attrs.validators.instance_of(str)])

    @classmethod
    def parse(cls, data: dict[str, Any]) -> CompanyOverview:
        return EarningsCalendar(**data)


EarningsCalendarList = NewType('EarningsCalendarList', list[EarningsCalendar])
