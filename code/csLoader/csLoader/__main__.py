# *******************************************************************************************
#  File:  __main__.py
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

import atexit
import os
import click
from pathlib import Path
import csCore.utils as utils
import src.config as config


@click.group("csLoader")
@click.pass_context
def cmd(ctx: click.Context) -> None:
    """
    This utility is used to init andreset the database as well as load the earnings file
    """
    config_folder = utils.find_config_folder()
    if not config_folder:
        raise ValueError('Config folder not found')
    config_file = config_folder.joinpath('cs_loader.cfg')
    if not config_file.exists():
        raise ValueError('Config folder not found')

    ctx.obj = config.load(config_file)


@cmd.command("init")
@click.pass_context
@click.argument('run_local', default=False, required=False)
def init(ctx, run_local: bool = False) -> None:
    """
    This command initializes the database
    """
    pass


@cmd.command("reset")
@click.pass_context
@click.argument('run_local', default=False, required=False)
def reset(ctx, run_local: bool = False) -> None:
    """
    This command resets the application database
    """
    pass


@cmd.command("set_config")
@click.option("-u", "--url", help="The url to connect to the application database", required=False)
def set_config(url: str | None = None) -> None:
    """
    This command sets the application configuration parameters
    """
    config_folder = utils.find_config_folder()
    if not config_folder:
        raise ValueError('Config folder not found')
    config_file = config_folder.joinpath('cs_loader.cfg')
    if not config_file.exists():
        raise ValueError('Config folder not found')

    if url:
        config.set_database_url(config_file, url)


@cmd.command("reset")
@click.pass_context
@click.argument('run_local', default=False, required=False)
def load_earnings(ctx: click.Context, run_local: bool = False) -> None:
    """
    This command loads the earnings file
    """
    pass


def exit_routine() -> None:
    try:
        utils.log_end()
    except:
        # We swallow any errors on exit
        pass


def main() -> None:
    # Set the working folder
    working_folder: Path = Path(__file__).parent
    os.chdir(working_folder)

    # Set up the exit routine
    atexit.register(exit_routine)

    # Configure logging
    utils.configure_logging('cs_core', __file__)
    utils.log_start()

    # Process command
    cmd(prog_name="csLoader")


if __name__ == '__main__':
    main()
