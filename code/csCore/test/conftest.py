# *******************************************************************************************
#  File:  conftest.py
#
#  Created: 30-05-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  30-05-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['alphavantage_key', 'openfigi_key']

import pytest


@pytest.fixture(scope="session")
def alphavantage_key() -> str:
    return 'TK7LTJYNCWD69QRH'


@pytest.fixture(scope="session")
def openfigi_key() -> str:
    return "fe11251c-d169-441b-bcf9-2afbc914d806"


@pytest.fixture(scope="session")
def sp100_url() -> str:
    return "https://en.wikipedia.org/wiki/S%26P_100"


@pytest.fixture(scope="session")
def sp600_url() -> str:
    return "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies"


@pytest.fixture(scope="session")
def sp400_url() -> str:
    return "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies"


@pytest.fixture(scope="session")
def sp500_url() -> str:
    return "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"


@pytest.fixture(scope="session")
def openfigi_url() -> str:
    return "https://api.openfigi.com/v1/mapping"


@pytest.fixture(scope="session")
def edgar_url() -> str:
    return "https://www.sec.gov/files/company_tickers_exchange.json"
