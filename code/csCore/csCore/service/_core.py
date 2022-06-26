# *******************************************************************************************
#  File:  _core.py
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
__all__ = ['get_page']

import requests
import csCore.errors as errors


def get_page(url: str) -> str:
    """
    This function downloads the page specified by the URL
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

    raise errors.RequestFailedError(url, response.status_code, response.text)
