# *******************************************************************************************
#  File:  _alphavantage.py
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
__all__ = ['AlphavantageService']

import csv
from io import StringIO

import orjson
import requests
import csCore.model.service as model
import csCore.errors as errors


class AlphavantageService:
    _key: str

    def __init__(self, key: str):
        self._key = key

    def _get_data(self, function: str, ticker: str) -> str:
        url = f"https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={self._key}"

        response = requests.get(url)

        if response.status_code != 200:
            raise errors.RequestFailedError(url, response.status_code, response.text)

        return response.text

    def _parse_company(self, value: str) -> model.CompanyOverview:
        data = orjson.loads(value)

        try:
            ticker = data['Symbol']
        except KeyError:
            raise errors.MaxLimitExceededError('', 0, 'API calls exceeded')

        name = data['Name']
        description = data['Description']
        exchange = data['Exchange']
        currency = data['Currency']
        country = data['Country']
        address = data['Address']
        fiscal_year_end = data['FiscalYearEnd']
        last_quarter = data['LatestQuarter']

        company = model.CompanyOverview(ticker, name, description, exchange, currency, country, address,
                                            fiscal_year_end, last_quarter)

        return company

    def _parse_earnings_file(self, data: str) -> model.EarningsCalendarList:
        def convert_estimate(value: str) -> int:
            if not value:
                value = '0'

            return int(float(value) * 100)

        source = StringIO(data)
        reader = csv.reader(source, delimiter=',')
        next(reader)

        earnings: model.EarningsCalendarList = list()

        for row in reader:
            ticker = row[0]
            name = row[1]
            report_date = row[2]
            fiscal_date_ending = row[3]
            estimate = convert_estimate(row[4])
            currency = row[5]

            earnings.append(model.EarningsCalendar(ticker, name, report_date, fiscal_date_ending, estimate, currency))

        if not earnings:
            errors.RequestFailedError('', 0, 'API calls exceeded')

        return earnings

    def _parse_earnings_statements(self, value: str) -> model.Statement:
        data = orjson.loads(value)

        # Make sure we have data
        if not 'symbol' in data:
            raise errors.RequestFailedError('', 0, 'API calls exceeded')

        annuals = data['annualEarnings']
        quarters = data['quarterlyEarnings']

        statements = model.Statement()

        for index, statement in enumerate(annuals):
            if index > 4:
                break

            for key, value in statement.items():
                if key not in statements.annual:
                    statements.annual[key] = model.AccountingItem(key)

                match index:
                    case 0:
                        statements.annual[key].value_1 = value
                    case 1:
                        statements.annual[key].value_2 = value
                    case 2:
                        statements.annual[key].value_3 = value
                    case 3:
                        statements.annual[key].value_4 = value
                    case 4:
                        statements.annual[key].value_5 = value

        for index, statement in enumerate(quarters):
            if index > 2:
                break

            for key, value in statement.items():
                if key not in statements.quarter:
                    statements.quarter[key] = model.AccountingItem(key)

                match index:
                    case 0:
                        statements.quarter[key].value_1 = value
                    case 1:
                        statements.quarter[key].value_2 = value
                    case 2:
                        statements.quarter[key].value_3 = value

        return statements

    def _parse_statements(self, value: str) -> model.Statement:
        data = orjson.loads(value)

        # Make sure we have data
        if not 'symbol' in data:
            raise errors.RequestFailedError('', 0, 'API calls exceeded')

        annuals = data['annualReports']
        quarters = data['quarterlyReports']

        statements = model.Statement()

        for index, statement in enumerate(annuals):
            if index > 4:
                break

            for key, value in statement.items():
                if key not in statements.annual:
                    statements.annual[key] = model.AccountingItem(key)

                match index:
                    case 0:
                        statements.annual[key].value_1 = value
                    case 1:
                        statements.annual[key].value_2 = value
                    case 2:
                        statements.annual[key].value_3 = value
                    case 3:
                        statements.annual[key].value_4 = value
                    case 4:
                        statements.annual[key].value_5 = value

        for index, statement in enumerate(quarters):
            if index > 2:
                break

            for key, value in statement.items():
                if key not in statements.quarter:
                    statements.quarter[key] = model.AccountingItem(key)

                match index:
                    case 0:
                        statements.quarter[key].value_1 = value
                    case 1:
                        statements.quarter[key].value_2 = value
                    case 2:
                        statements.quarter[key].value_3 = value

        return statements

    def get_income(self, ticker: str) -> model.Statement:
        data = self._get_data('INCOME_STATEMENT', ticker)
        return self._parse_statements(data)

    def get_cash_flow(self, ticker: str) -> model.Statement:
        data = self._get_data('CASH_FLOW', ticker)
        return self._parse_statements(data)

    def get_balance_sheet(self, ticker: str) -> model.Statement:
        data = self._get_data('BALANCE_SHEET', ticker)
        return self._parse_statements(data)

    def get_earnings(self, ticker: str) -> model.Statement:
        data = self._get_data('EARNINGS', ticker)
        return self._parse_earnings_statements(data)

    def get_company(self, ticker: str) -> model.CompanyOverview:
        data = self._get_data('OVERVIEW', ticker)
        record_data = orjson.loads(data)
        return model.CompanyOverview.parse(record_data)

    def get_estimates(self) -> model.EarningsCalendarList:
        url = f"https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={self._key}"
        response = requests.get(url)

        if response.status_code != 200:
            raise errors.RequestFailedError(url, response.status_code, response.text)

        return self._parse_earnings_file(response.text)

