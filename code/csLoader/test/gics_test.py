# *******************************************************************************************
#  File:  gics_test.py
#
#  Created: 01-07-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  01-07-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

import csLoader.src.gics as gics


def test_load_gics() -> None:
    data = gics.load_gics()
    assert len(data) == 11
