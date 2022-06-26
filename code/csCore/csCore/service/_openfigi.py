# *******************************************************************************************
#  File:  _openfigi.py
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
__all__ = ['OpenFigiService']

import orjson
import requests
import csCore.model.service as model
import csCore.errors as error

class OpenFigiService:
    _key: str
    _url: str

    def __init__(self, key: str, url: str) -> object:
        self._key = key
        self._url = url

    def get_codes(self, tickers: list[str]) -> list[model.FigiCode] | None:
        query = [{'idType': 'TICKER', 'idValue': ticker, 'exchCode': 'US'} for ticker in tickers]
        headers = {'Content-Type': 'text/json', 'X-OPENFIGI-APIKEY': self._key}

        response = requests.post(url=self._url, headers=headers, json=query)

        if response.status_code == 429:
            raise error.MaxLimitExceededError(self._url, response.status_code, response.text)

        if response.status_code != 200:
            raise error.RequestFailedError(self._url, response.status_code, response.text)

        content = orjson.loads(response.text)

        if 'error' in content[0]:
            msg: str = content[0]['error']
            if msg == 'No identifier found.':
                return None
            raise error.ResponseError(self._url, response.status_code,
                                      f"Error while seeking FIGI code for: {' '.join(tickers)} - {msg}")

        records: list[model.FigiCode] = list()
        for index, row in enumerate(content):
            if 'error' in row:
                msg = row['error']
                if msg == 'No identifier found.':
                    records.append(model.FigiCode(tickers[index], ''))
                    continue
                raise ValueError(f"Unexpected response from OpenFIGI API: {tickers[index]} - {msg}")

            ticker = row['data'][0]['ticker']
            figi = row['data'][0]['figi']
            records.append(model.FigiCode(ticker, figi))

        return records
