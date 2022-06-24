# *******************************************************************************************
#  File:  service_test.py
#
#  Created: 24-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  24-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

import attrs
import orjson
import pendulum

import csCore.model.service as svc_model


class TestFigiCode:
    def test_create(self) -> None:
        record = svc_model.FigiCode('IBM', '34567')
        assert record.ticker == 'IBM'
        assert record.figi == '000000034567'

    def test_parse(self) -> None:
        raw_data = """
            {
                "ticker":"IBM",
                "figi":"34567"
            }
        """

        data = orjson.loads(raw_data)

        record = svc_model.FigiCode.parse(data)
        assert record.ticker == 'IBM'
        assert record.figi == '000000034567'


class TestCikCode:
    def test_create(self) -> None:
        record = svc_model.CikCode('789', 'IBM', 'IBM Corp.', 'NYSE')
        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert record.cik == '0000000789'
        assert record.exchange == 'NYSE'

    def test_parse(self) -> None:
        raw_data = """
            {
                "cik":"789",
                "ticker":"IBM",
                "name":"IBM Corp.",
                "exchange":"NYSE"
            }
        """

        data = orjson.loads(raw_data)

        record = svc_model.CikCode.parse(data)
        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert record.cik == '0000000789'
        assert record.exchange == 'NYSE'


class TestSpComponent:
    def test_create(self) -> None:
        record = svc_model.SpComponent('IBM', 'IBM Corp.', 'Sector', 'Sub Industry')
        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert record.sector == 'Sector'
        assert record.sub_industry == 'Sub Industry'

    def test_parse(self) -> None:
        raw_data = """
            {
                "ticker":"IBM",
                "name":"IBM Corp.",
                "sector":"Sector",
                "sub_industry":"Sub Industry"
            }
        """

        data = orjson.loads(raw_data)
        record = svc_model.SpComponent.parse(data)
        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert record.sector == 'Sector'
        assert record.sub_industry == 'Sub Industry'


class TestAccountingItem:
    def test_create(self) -> None:
        record = svc_model.AccountingItem('Revenue', '234', '67', '57', '90', '34')

        assert record.tag == 'Revenue'
        assert record.value_1 == '234'
        assert record.value_2 == '67'
        assert record.value_3 == '57'
        assert record.value_4 == '90'
        assert record.value_5 == '34'

    def test_parse(self) -> None:
        raw_data = """
            {
                "tag":"Revenue",
                "value_1":"234",
                "value_2":"67",
                "value_3":"57",
                "value_4":"90",
                "value_5":"34"
            }
        """

        data = orjson.loads(raw_data)

        record = svc_model.AccountingItem.parse(data)
        assert record.tag == 'Revenue'
        assert record.value_1 == '234'
        assert record.value_2 == '67'
        assert record.value_3 == '57'
        assert record.value_4 == '90'
        assert record.value_5 == '34'


class TestStatement:
    def test_create(self) -> None:
        record = svc_model.Statement()
        assert len(record.annual) == 0
        assert len(record.quarter) == 0

    def test_parse(self) -> None:
        raw_data = """
            {
                "annual":[
                    {
                        "tag":"Revenue",
                        "value_1":"234",
                        "value_2":"67",
                        "value_3":"57",
                        "value_4":"90",
                        "value_5":"34"
                    },
                    {
                        "tag":"Revenue",
                        "value_1":"234",
                        "value_2":"67",
                        "value_3":"57",
                        "value_4":"90",
                        "value_5":"34"
                    }
                ],
                "quarter":[
                    {
                        "tag":"Revenue",
                        "value_1":"234",
                        "value_2":"67",
                        "value_3":"57",
                        "value_4":"90",
                        "value_5":"34"
                    },
                    {
                        "tag":"Revenue",
                        "value_1":"234",
                        "value_2":"67",
                        "value_3":"57",
                        "value_4":"90",
                        "value_5":"34"
                    }
                ]
            }
        """
        data = orjson.loads(raw_data)

        record = svc_model.Statement.parse(data)
        assert len(record.annual) == 2
        assert len(record.quarter) == 2


class TestFinancialStatements:
    def test_create(self) -> None:
        record = svc_model.FinancialStatements('IBM', 'IBM Corp.')

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert len(record.income.annual) == 0
        assert len(record.income.quarter) == 0
        assert len(record.cash_flow.annual) == 0
        assert len(record.cash_flow.quarter) == 0
        assert len(record.balance_sheet.annual) == 0
        assert len(record.balance_sheet.quarter) == 0
        assert len(record.earnings.annual) == 0
        assert len(record.earnings.quarter) == 0

    def test_parse(self) -> None:
        raw_data = """
            {
                "ticker":"IBM",
                "name":"IBM Corp.",
                "income": {
                    "annual":[
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        },
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        }
                    ],
                    "quarter":[
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        },
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        }
                    ]
                },
                "cash_flow": {
                    "annual":[
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        },
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        }
                    ],
                    "quarter":[
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        },
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        }
                    ]
                },
                "balance_sheet": {
                    "annual":[
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        },
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        }
                    ],
                    "quarter":[
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        },
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        }
                    ]
                },
                "earnings": {
                    "annual":[
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        },
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        }
                    ],
                    "quarter":[
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        },
                        {
                            "tag":"Revenue",
                            "value_1":"234",
                            "value_2":"67",
                            "value_3":"57",
                            "value_4":"90",
                            "value_5":"34"
                        }
                    ]
                }
            }
        """

        data = orjson.loads(raw_data)
        record = svc_model.FinancialStatements.parse(data)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert len(record.income.annual) == 2
        assert len(record.income.quarter) == 2
        assert len(record.cash_flow.annual) == 2
        assert len(record.cash_flow.quarter) == 2
        assert len(record.balance_sheet.annual) == 2
        assert len(record.balance_sheet.quarter) == 2
        assert len(record.earnings.annual) == 2
        assert len(record.earnings.quarter) == 2


class TestCompany:
    def test_create(self) -> None:
        record = svc_model.CompanyOverview('IBM', 'IBM Corp.', 'IBM Company Description', '345', 'NYSE', 'USD', 'US',
                                           'Technology', 'Software', '1 Main Street', 'May')

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert record.description == 'IBM Company Description'
        assert record.cik == '0000000345'
        assert record.exchange == 'NYSE'
        assert record.currency == 'USD'
        assert record.country == 'US'
        assert record.sector == 'Technology'
        assert record.industry == 'Software'
        assert record.address == '1 Main Street'
        assert record.fiscal_year_end == 'May'

    def test_parse(self) -> None:
        raw_data = """
            {
                "ticker":"IBM",
                "name":"IBM Corp.",
                "description":"IBM Company Description",
                "cik":"345",
                "exchange":"NYSE",
                "currency":"USD",
                "country":"US",
                "sector":"Technology",
                "industry":"Software",
                "address":"1 Main Street",
                "fiscal_year_end":"May"
            }
        """

        data = orjson.loads(raw_data)
        record = svc_model.CompanyOverview.parse(data)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert record.description == 'IBM Company Description'
        assert record.cik == '0000000345'
        assert record.exchange == 'NYSE'
        assert record.currency == 'USD'
        assert record.country == 'US'
        assert record.sector == 'Technology'
        assert record.industry == 'Software'
        assert record.address == '1 Main Street'
        assert record.fiscal_year_end == 'May'


class TestEarningsCalendar:
    def test_create(self) -> None:
        record = svc_model.EarningsCalendar('IBM', 'IBM Corp.', '2022-06-16T16:28:29.940+00:00',
                                            '2022-06-16T16:28:29.940+00:00', 234, 'USD')

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert record.report_date == pendulum.parse('2022-06-16T16:28:29.940+00:00', strict=False)
        assert record.fiscal_date_ending == pendulum.parse('2022-06-16T16:28:29.940+00:00', strict=False)
        assert record.estimate == 234
        assert record.currency == 'USD'

    def test_parse(self) -> None:
        raw_data = """
            {
                "ticker":"IBM",
                "name":"IBM Corp.",
                "report_date":"2022-06-16T16:28:29.940+00:00",
                "fiscal_date_ending":"2022-06-16T16:28:29.940+00:00",
                "estimate": 234,
                "currency":"USD"
            }
        """

        data = orjson.loads(raw_data)
        record = svc_model.EarningsCalendar.parse(data)

        assert record.ticker == 'IBM'
        assert record.name == 'IBM Corp.'
        assert record.report_date == pendulum.parse('2022-06-16T16:28:29.940+00:00', strict=False)
        assert record.fiscal_date_ending == pendulum.parse('2022-06-16T16:28:29.940+00:00', strict=False)
        assert record.estimate == 234
        assert record.currency == 'USD'
