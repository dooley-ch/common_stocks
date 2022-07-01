# *******************************************************************************************
#  File:  config.py
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
__all__ = ['load', 'set_database_url']

import configparser
from pathlib import Path
from typing import Any


def load(config_file: Path) -> dict[str, Any]:
    """
    This function loads the application configuration from the config file
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    db_url = config['database']['url']

    config_dict = dict()
    config_dict['url'] = db_url

    return config_dict


def set_database_url(config_file: Path, url: str) -> None:
    """
    This function stores the database url in the application's config file
    """
    config = configparser.ConfigParser()
    config.read(config_file)

    config['database']['url'] = url

    with config_file.open('w') as f:
        config.write(f)
