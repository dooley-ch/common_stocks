# *******************************************************************************************
#  File:  _wikipedia.py
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
__all__ = ['WikipediaService']

import bs4

import csCore.model.service as model
from ._core import get_page


class WikipediaService:
    _url_sp100: str
    _url_sp400: str
    _url_sp600: str
    _url_sp500: str

    def __init__(self, url_sp100: str, url_sp400: str, url_sp600: str, url_sp500: str) -> object:
        self._url_sp100 = url_sp100
        self._url_sp400 = url_sp400
        self._url_sp600 = url_sp600
        self._url_sp500 = url_sp500

    def get_sp600(self) -> model.SpComponentList | None:
        contents = get_page(self._url_sp600)

        if contents:
            components: model.SpComponentList = list()

            soup = bs4.BeautifulSoup(contents, 'html.parser')
            table = soup.find('table', attrs={'id': 'constituents'})
            if table:
                tbody = table.find('tbody')
                if tbody:
                    rows = tbody.find_all('tr')
                    if rows:
                        for row in rows:
                            name = str(row.contents[1].text).strip()
                            ticker = str(row.contents[3].text).strip()
                            sub_industry = str(row.contents[7].text).strip()
                            cik = str(row.contents[11].text).strip()

                            if name == 'Company':
                                continue

                            components.append(model.SpComponent(ticker, name, cik, sub_industry))
            return components

    def get_sp400(self) -> model.SpComponentList | None:
        contents = get_page(self._url_sp400)

        if contents:
            components: model.SpComponentList = list()

            soup = bs4.BeautifulSoup(contents, 'html.parser')
            table = soup.find('table', attrs={'id': 'constituents'})
            if table:
                tbody = table.find('tbody')
                if tbody:
                    rows = tbody.find_all('tr')
                    if rows:
                        for row in rows:
                            name = str(row.contents[1].text).strip()
                            ticker = str(row.contents[3].text).strip()
                            sub_industry = str(row.contents[7].text).strip()

                            if name == 'Security':
                                continue

                            components.append(model.SpComponent(ticker, name, '0000000000', sub_industry))
            return components

    def get_sp500(self) -> model.SpComponentList | None:
        contents = get_page(self._url_sp500)

        if contents:
            components: model.SpComponentList = list()

            soup = bs4.BeautifulSoup(contents, 'html.parser')
            table = soup.find('table', attrs={'id': 'constituents'})
            if table:
                tbody = table.find('tbody')
                if tbody:
                    rows = tbody.find_all('tr')
                    if rows:
                        for row in rows:
                            name = str(row.contents[3].text).strip()
                            ticker = str(row.contents[1].text).strip()
                            sub_industry = str(row.contents[9].text).strip()
                            cik = str(row.contents[15].text).strip()

                            if name == 'Security':
                                continue

                            components.append(model.SpComponent(ticker, name, cik, sub_industry))
            return components

    def get_sp100(self) -> list[str] | None:
        contents = get_page(self._url_sp100)

        if contents:
            components: list[str] = list()

            soup = bs4.BeautifulSoup(contents, 'html.parser')
            table = soup.find('table', attrs={'id': 'constituents'})
            if table:
                tbody = table.find('tbody')
                if tbody:
                    rows = tbody.find_all('tr')
                    if rows:
                        for row in rows:
                            name = str(row.contents[3].text).strip()
                            ticker = str(row.contents[1].text).strip()

                            if name == 'Name':
                                continue

                            components.append(ticker)
            return components
