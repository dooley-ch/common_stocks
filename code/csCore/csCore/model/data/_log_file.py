# *******************************************************************************************
#  File:  _log_file.py
#
#  Created: 22-06-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  22-06-2022: Initial version
#
# *******************************************************************************************
from __future__ import annotations

__author__ = "James Dooley"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"
__all__ = ['LogLevel', 'CSApiActivityLog', 'CSApiActivityLogList', 'CSApiLog', 'CSApiLogList', 'CSLoaderActivityLog',
           'CSLoaderActivityLogList', 'CSLoaderLog', 'CSLoaderLogList', 'CSQueueActivityLog', 'CSQueueActivityLogList',
           'CSQueueLog', 'CSQueueLogList', 'CSWebAppActivityLog', 'CSWebAppActivityLogList', 'CSWebAppLog',
           'CSWebAppLogList']

from datetime import datetime
from enum import Enum
from typing import Any, TypeVar, NewType
import attrs
from ._core import parse_record_date

T = TypeVar('T')


class LogLevel(str, Enum):
    trace = 'TRACE'
    debug = 'DEBUG'
    info = 'INFO'
    success = 'SUCCESS'
    warning = 'WARNING'
    error = 'ERROR'
    critical = 'CRITICAL'


@attrs.frozen
class _Log:
    message: str = attrs.field(validator=[attrs.validators.instance_of(str)])
    level: LogLevel = attrs.field(default=LogLevel.error, converter=lambda value: LogLevel(value),
                                  validator=[attrs.validators.instance_of(LogLevel)])
    logged_at: datetime = attrs.field(factory=datetime.now, validator=[attrs.validators.instance_of(datetime)],
                                      converter=parse_record_date)
    function: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    file: str = attrs.field(default='', validator=[attrs.validators.instance_of(str)])
    line: int = attrs.field(default=0, validator=[attrs.validators.instance_of(int)])

    @classmethod
    def _internal_parse(cls, data: dict[str, Any], return_type: T) -> T:
        return return_type(**data)


@attrs.frozen
class CSApiActivityLog(_Log):
    @classmethod
    def parse(cls, data: dict[str, Any]) -> CSApiActivityLog:
        return super()._internal_parse(data, CSApiActivityLog)


CSApiActivityLogList = NewType('CSApiActivityLogList', list[CSApiActivityLog])


@attrs.frozen
class CSApiLog(_Log):
    @classmethod
    def parse(cls, data: dict[str, Any]) -> CSApiLog:
        return super()._internal_parse(data, CSApiLog)


CSApiLogList = NewType('CSApiLogList', list[CSApiLog])


@attrs.frozen
class CSLoaderActivityLog(_Log):
    @classmethod
    def parse(cls, data: dict[str, Any]) -> CSLoaderActivityLog:
        return super()._internal_parse(data, CSLoaderActivityLog)


CSLoaderActivityLogList = NewType('CSLoaderActivityLogList', list[CSLoaderActivityLog])


@attrs.frozen
class CSLoaderLog(_Log):
    @classmethod
    def parse(cls, data: dict[str, Any]) -> CSLoaderLog:
        return super()._internal_parse(data, CSLoaderLog)


CSLoaderLogList = NewType('CSLoaderActivityLogList', list[CSLoaderLog])


@attrs.frozen
class CSQueueActivityLog(_Log):
    @classmethod
    def parse(cls, data: dict[str, Any]) -> CSQueueActivityLog:
        return super()._internal_parse(data, CSQueueActivityLog)


CSQueueActivityLogList = NewType('CSQueueActivityLogList', list[CSQueueActivityLog])


@attrs.frozen
class CSQueueLog(_Log):
    @classmethod
    def parse(cls, data: dict[str, Any]) -> CSQueueLog:
        return super()._internal_parse(data, CSQueueLog)


CSQueueLogList = NewType('CSQueueLogList', list[CSQueueLog])


@attrs.frozen
class CSWebAppActivityLog(_Log):
    @classmethod
    def parse(cls, data: dict[str, Any]) -> CSWebAppActivityLog:
        return super()._internal_parse(data, CSWebAppActivityLog)


CSWebAppActivityLogList = NewType('CSWebAppActivityLogList', list[CSWebAppActivityLog])


@attrs.frozen
class CSWebAppLog(_Log):
    @classmethod
    def parse(cls, data: dict[str, Any]) -> CSWebAppLog:
        return super()._internal_parse(data, CSWebAppLog)


CSWebAppLogList = NewType('CSWebAppLogList', list[CSWebAppLog])
