# *******************************************************************************************
#  File:  financial_statements_test.py
#
#  Created: 21-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  21-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

import orjson
import csCore.model.data as db_model

_financial_statements_data_1 = """
    {
        "ticker":"IBM",
        "name":"IBM Corp.",
        "income_statement_annual": [
            {"tag":"Revenue", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"COS", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "income_statement_quarter": [
            {"tag":"Revenue", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"COS", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "cash_flow_statement_annual": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"NetCash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "cash_flow_statement_quarter": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"NetCash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "balance_sheet_statement_annual": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"Debtors", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "balance_sheet_statement_quarter": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"Debtors", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],     
        "earnings_statement_annual": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "earnings_statement_quarter": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ]
    }
"""

_financial_statements_data_2 = """
    {
        "ticker":"IBM",
        "name":"IBM Corp.",
        "income_statement_annual": [
            {"tag":"Revenue", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"COS", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "income_statement_quarter": [
            {"tag":"Revenue", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"COS", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "cash_flow_statement_annual": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"NetCash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "cash_flow_statement_quarter": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"NetCash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "balance_sheet_statement_annual": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"Debtors", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "balance_sheet_statement_quarter": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"},
            {"tag":"Debtors", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],     
        "earnings_statement_annual": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],
        "earnings_statement_quarter": [
            {"tag":"Cash", "value_1":"23", "value_2":"45", "value_3":"35", "value_4":"3", "value_5":"3"}
        ],           
        "metadata": {
            "lock_version": 1,
            "created_at": "2022-06-16T16:28:29.940+00:00",
            "updated_at": "2022-06-16T16:28:29.940+00:00"
        }
    }
"""


class TestFinancialStatements:
    """
    This class tests the Financial Statements DTO class
    """

    def test_create_minimum(self) -> None:
        record = db_model.FinancialStatements('IBM', 'IBM Corp')

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp'

    def test_create(self) -> None:
        record = db_model.FinancialStatements('IBM', 'IBM Corp')

        record.income_statement_annual.append(db_model.AccountsEntry('Revenue'))
        record.income_statement_annual.append(db_model.AccountsEntry('COS'))
        record.income_statement_quarter.append(db_model.AccountsEntry('Revenue'))
        record.income_statement_quarter.append(db_model.AccountsEntry('COS'))

        record.cash_flow_statement_annual.append(db_model.AccountsEntry('OpeningBalance'))
        record.cash_flow_statement_annual.append(db_model.AccountsEntry('NetCash'))
        record.cash_flow_statement_quarter.append(db_model.AccountsEntry('OpeningBalance'))
        record.cash_flow_statement_quarter.append(db_model.AccountsEntry('NetCash'))

        record.balance_sheet_statement_annual.append(db_model.AccountsEntry('Cash'))
        record.balance_sheet_statement_annual.append(db_model.AccountsEntry('Debtors'))
        record.balance_sheet_statement_quarter.append(db_model.AccountsEntry('Cash'))
        record.balance_sheet_statement_quarter.append(db_model.AccountsEntry('Debtors'))

        record.earnings_statement_annual.append(db_model.AccountsEntry("Earnings"))
        record.earnings_statement_quarter.append(db_model.AccountsEntry("Earnings"))

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp'
        assert len(record.income_statement_annual) == 2
        assert len(record.income_statement_quarter) == 2
        assert len(record.cash_flow_statement_annual) == 2
        assert len(record.cash_flow_statement_quarter) == 2
        assert len(record.earnings_statement_annual) == 1
        assert len(record.earnings_statement_quarter) == 1

    def test_create_ext(self) -> None:
        record = db_model.FinancialStatementsExt('IBM', 'IBM Corp')

        record.income_statement_annual.append(db_model.AccountsEntry('Revenue'))
        record.income_statement_annual.append(db_model.AccountsEntry('COS'))
        record.income_statement_quarter.append(db_model.AccountsEntry('Revenue'))
        record.income_statement_quarter.append(db_model.AccountsEntry('COS'))

        record.cash_flow_statement_annual.append(db_model.AccountsEntry('OpeningBalance'))
        record.cash_flow_statement_annual.append(db_model.AccountsEntry('NetCash'))
        record.cash_flow_statement_quarter.append(db_model.AccountsEntry('OpeningBalance'))
        record.cash_flow_statement_quarter.append(db_model.AccountsEntry('NetCash'))

        record.balance_sheet_statement_annual.append(db_model.AccountsEntry('Cash'))
        record.balance_sheet_statement_annual.append(db_model.AccountsEntry('Debtors'))
        record.balance_sheet_statement_quarter.append(db_model.AccountsEntry('Cash'))
        record.balance_sheet_statement_quarter.append(db_model.AccountsEntry('Debtors'))

        record.earnings_statement_annual.append(db_model.AccountsEntry("Earnings"))
        record.earnings_statement_quarter.append(db_model.AccountsEntry("Earnings"))

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp'
        assert len(record.income_statement_annual) == 2
        assert len(record.income_statement_quarter) == 2
        assert len(record.cash_flow_statement_annual) == 2
        assert len(record.cash_flow_statement_quarter) == 2
        assert len(record.earnings_statement_annual) == 1
        assert len(record.earnings_statement_quarter) == 1
        assert record.metadata.lock_version == 1

    def test_parse(self) -> None:
        data = orjson.loads(_financial_statements_data_1)
        record = db_model.FinancialStatements.parse(data)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'

    def test_parse_ext(self) -> None:
        data = orjson.loads(_financial_statements_data_2)
        record = db_model.FinancialStatementsExt.parse(data)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert record.metadata.lock_version == 1
