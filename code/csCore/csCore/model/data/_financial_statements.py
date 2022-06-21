# *******************************************************************************************
#  File:  _financial_statements.py
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
__all__ = ['AccountsEntry', 'AccountsEntryList', 'FinancialStatements', 'FinancialStatementsExt']

from typing import NewType, Any
import attrs
from ._core import Metadata


@attrs.frozen
class AccountsEntry:
    tag: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    value_1: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    value_2: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    value_3: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    value_4: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    value_5: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])


AccountsEntryList = NewType('ConfigItemList', list[AccountsEntry])

@attrs.frozen
class FinancialStatements:
    ticker: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    name: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    income_statement_annual: AccountsEntryList = attrs.Factory(list)
    income_statement_quarter: AccountsEntryList = attrs.Factory(list)
    cash_flow_statement_annual: AccountsEntryList = attrs.Factory(list)
    cash_flow_statement_quarter: AccountsEntryList = attrs.Factory(list)
    balance_sheet_statement_annual: AccountsEntryList = attrs.Factory(list)
    balance_sheet_statement_quarter: AccountsEntryList = attrs.Factory(list)
    earnings_statement_annual: AccountsEntryList = attrs.Factory(list)
    earnings_statement_quarter: AccountsEntryList = attrs.Factory(list)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> FinancialStatements:
        ticker = data['ticker']
        name = data['name']
        inc_annual = data['income_statement_annual']
        inc_quarter = data['income_statement_quarter']
        cf_annual = data['cash_flow_statement_annual']
        cf_quarter = data['cash_flow_statement_quarter']
        bs_annual = data['balance_sheet_statement_annual']
        bs__quarter = data['balance_sheet_statement_quarter']
        earnings_annual = data['earnings_statement_annual']
        earnings_quarter = data['earnings_statement_quarter']

        record = FinancialStatements(ticker, name)

        for item in inc_annual:
            record.income_statement_annual.append(AccountsEntry(**item))
        for item in inc_quarter:
            record.income_statement_quarter.append(AccountsEntry(**item))

        for item in cf_annual:
            record.cash_flow_statement_annual.append(AccountsEntry(**item))
        for item in cf_quarter:
            record.cash_flow_statement_quarter.append(AccountsEntry(**item))

        for item in bs_annual:
            record.balance_sheet_statement_annual.append(AccountsEntry(**item))
        for item in bs__quarter:
            record.balance_sheet_statement_quarter.append(AccountsEntry(**item))

        for item in earnings_annual:
            record.earnings_statement_annual.append(AccountsEntry(**item))
        for item in earnings_quarter:
            record.earnings_statement_quarter.append(AccountsEntry(**item))

        return record


@attrs.frozen
class FinancialStatementsExt(FinancialStatements):
    metadata: Metadata = attrs.Factory(Metadata)

    @classmethod
    def parse(cls, data: dict[str, Any]) -> FinancialStatementsExt:
        ticker = data['ticker']
        name = data['name']
        inc_annual = data['income_statement_annual']
        inc_quarter = data['income_statement_quarter']
        cf_annual = data['cash_flow_statement_annual']
        cf_quarter = data['cash_flow_statement_quarter']
        bs_annual = data['balance_sheet_statement_annual']
        bs__quarter = data['balance_sheet_statement_quarter']
        earnings_annual = data['earnings_statement_annual']
        earnings_quarter = data['earnings_statement_quarter']
        metadata = data['metadata']

        record = FinancialStatementsExt(ticker, name, metadata=Metadata(**metadata))

        for item in inc_annual:
            record.income_statement_annual.append(AccountsEntry(**item))
        for item in inc_quarter:
            record.income_statement_quarter.append(AccountsEntry(**item))

        for item in cf_annual:
            record.cash_flow_statement_annual.append(AccountsEntry(**item))
        for item in cf_quarter:
            record.cash_flow_statement_quarter.append(AccountsEntry(**item))

        for item in bs_annual:
            record.balance_sheet_statement_annual.append(AccountsEntry(**item))
        for item in bs__quarter:
            record.balance_sheet_statement_quarter.append(AccountsEntry(**item))

        for item in earnings_annual:
            record.earnings_statement_annual.append(AccountsEntry(**item))
        for item in earnings_quarter:
            record.earnings_statement_quarter.append(AccountsEntry(**item))

        return record
