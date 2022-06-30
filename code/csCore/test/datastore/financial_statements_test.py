# *******************************************************************************************
#  File:  financial_statements_test.py
#
#  Created: 30-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  30-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

import csCore.datastore as ds
import csCore.model.data as model


class TestFinancialStatements:
    def test_insert(self, mongodb_connection, database_name) -> None:
        store = ds.FinancialStatementsStore(mongodb_connection, database_name)
        store.clear()

        record = model.FinancialStatementsExt('IBM', 'IBM Corp')

        record.income_statement_annual.append(model.AccountsEntry('Revenue'))
        record.income_statement_annual.append(model.AccountsEntry('COS'))
        record.income_statement_quarter.append(model.AccountsEntry('Revenue'))
        record.income_statement_quarter.append(model.AccountsEntry('COS'))

        record.cash_flow_statement_annual.append(model.AccountsEntry('OpeningBalance'))
        record.cash_flow_statement_annual.append(model.AccountsEntry('NetCash'))
        record.cash_flow_statement_quarter.append(model.AccountsEntry('OpeningBalance'))
        record.cash_flow_statement_quarter.append(model.AccountsEntry('NetCash'))

        record.balance_sheet_statement_annual.append(model.AccountsEntry('Cash'))
        record.balance_sheet_statement_annual.append(model.AccountsEntry('Debtors'))
        record.balance_sheet_statement_quarter.append(model.AccountsEntry('Cash'))
        record.balance_sheet_statement_quarter.append(model.AccountsEntry('Debtors'))

        record.earnings_statement_annual.append(model.AccountsEntry("Earnings"))
        record.earnings_statement_quarter.append(model.AccountsEntry("Earnings"))

        assert store.insert(record)

    def test_get(self, mongodb_connection, database_name) -> None:
        store = ds.FinancialStatementsStore(mongodb_connection, database_name)
        store.clear()

        record = model.FinancialStatementsExt('IBM', 'IBM Corp')

        record.income_statement_annual.append(model.AccountsEntry('Revenue'))
        record.income_statement_annual.append(model.AccountsEntry('COS'))
        record.income_statement_quarter.append(model.AccountsEntry('Revenue'))
        record.income_statement_quarter.append(model.AccountsEntry('COS'))

        record.cash_flow_statement_annual.append(model.AccountsEntry('OpeningBalance'))
        record.cash_flow_statement_annual.append(model.AccountsEntry('NetCash'))
        record.cash_flow_statement_quarter.append(model.AccountsEntry('OpeningBalance'))
        record.cash_flow_statement_quarter.append(model.AccountsEntry('NetCash'))

        record.balance_sheet_statement_annual.append(model.AccountsEntry('Cash'))
        record.balance_sheet_statement_annual.append(model.AccountsEntry('Debtors'))
        record.balance_sheet_statement_quarter.append(model.AccountsEntry('Cash'))
        record.balance_sheet_statement_quarter.append(model.AccountsEntry('Debtors'))

        record.earnings_statement_annual.append(model.AccountsEntry("Earnings"))
        record.earnings_statement_quarter.append(model.AccountsEntry("Earnings"))

        assert store.insert(record)

        record = store.get('IBM')

        assert record.name == 'IBM Corp'
