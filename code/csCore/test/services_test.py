# *******************************************************************************************
#  File:  services_test.py
#
#  Created: 26-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  26-06-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

import pytest

import csCore.service as svc


class TestWikipediaService:
    def test_get_sp600(self, sp100_url, sp400_url, sp600_url, sp500_url) -> None:
        service = svc.WikipediaService(sp100_url, sp400_url, sp600_url, sp500_url)
        records = service.get_sp600()
        assert len(records) > 599

    def test_get_sp400(self, sp100_url, sp400_url, sp600_url, sp500_url) -> None:
        service = svc.WikipediaService(sp100_url, sp400_url, sp600_url, sp500_url)
        records = service.get_sp400()
        assert len(records) > 399

    def test_get_sp500(self, sp100_url, sp400_url, sp600_url, sp500_url) -> None:
        service = svc.WikipediaService(sp100_url, sp400_url, sp600_url, sp500_url)
        records = service.get_sp500()
        assert len(records) > 499

    def test_get_sp100(self, sp100_url, sp400_url, sp600_url, sp500_url) -> None:
        service = svc.WikipediaService(sp100_url, sp400_url, sp600_url, sp500_url)
        records = service.get_sp100()
        assert len(records) > 99


class TestOpenFigiService:
    def test_valid_values(self, openfigi_key, openfigi_url) -> None:
        service = svc.OpenFigiService(openfigi_key, openfigi_url)

        codes = service.get_codes(['IBM', 'JNJ', 'AAPL'])
        assert len(codes) == 3

    def test_missing_value(self, openfigi_key, openfigi_url) -> None:
        service = svc.OpenFigiService(openfigi_key, openfigi_url)

        codes = service.get_codes(['IBM', 'JNJ', 'AAPL', 'XX45'])
        assert len(codes) == 4

        entry = codes[3]
        assert entry.ticker == 'XX45' and entry.figi == '000000000000'


class TestEdgarSecService:
    def test_get_codes(self, edgar_url) -> None:
        service = svc.EdgarSecService(edgar_url)
        records = service.get_codes()
        assert len(records) > 12_000


@pytest.mark.skip(reason='This API is limited to 5 calls per minute.')
class TestAlphavantageService:
    def test_get_company(self, alphavantage_key) -> None:
        service = svc.AlphavantageService(alphavantage_key)
        record = service.get_company('IBM')
        assert record.ticker == 'IBM'
        assert record.name == 'International Business Machines'

    def test_get_earnings_estimates(self, alphavantage_key) -> None:
        service = svc.AlphavantageService(alphavantage_key)
        records = service.get_estimates()
        assert len(records) > 5000

    def test_get_income_statement(self, alphavantage_key) -> None:
        service = svc.AlphavantageService(alphavantage_key)
        data = service.get_income('IBM')
        assert len(data.annual) > 20
        assert len(data.quarter) > 20

    def test_get_cash_flow_statement(self, alphavantage_key) -> None:
        service = svc.AlphavantageService(alphavantage_key)
        data = service.get_cash_flow('IBM')
        assert len(data.annual) > 20
        assert len(data.quarter) > 20

    def test_get_balance_sheet_statement(self, alphavantage_key) -> None:
        service = svc.AlphavantageService(alphavantage_key)
        data = service.get_balance_sheet('IBM')
        assert len(data.annual) > 20
        assert len(data.quarter) > 20

    def test_get_earnings_statement(self, alphavantage_key) -> None:
        service = svc.AlphavantageService(alphavantage_key)
        data = service.get_earnings('IBM')
        assert len(data.annual) >= 2
        assert len(data.quarter) >= 6
