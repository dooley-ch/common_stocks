# *******************************************************************************************
#  File:  errors.py
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
__all__ = ['ApplicationError', 'ServiceError', 'DatastoreError', 'MessageQueueError', 'MaxLimitExceededError',
           'RequestFailedError', 'ResponseError', 'ResponseParseError', 'DuplicateKeyError']

from typing import Any


class ApplicationError(Exception):
    """
    Base class for all application errors
    """
    pass


class ServiceError(ApplicationError):
    """
    Base class for all service errors
    """
    _url: str
    _status_code: int
    _message: str

    def __init__(self, url: str, status_code: int, message: str):
        self._url = url
        self._status_code = status_code
        self._message = message


    def __repr__(self) -> object:
        return f"url: {self._url} - status code: {self._status_code} - message: {self._message}"


class MaxLimitExceededError(ServiceError):
    def __init__(self, url: str, status_code: int, message: str) -> object:
        super().__init__(url, status_code, message)


class RequestFailedError(ServiceError):
    def __init__(self, url: str, status_code: int, message: str) -> object:
        super().__init__(url, status_code, message)


class ResponseError(ServiceError):
    def __init__(self, url: str, status_code: int, message: str) -> object:
        super().__init__(url, status_code, message)


class ResponseParseError(ServiceError):
    def __init__(self, message: str) -> object:
        super().__init__('', 0, message)


class DatastoreError(ApplicationError):
    """
    Base class for all datastore errors
    """
    pass


class DuplicateKeyError(DatastoreError):
    """
    This class is raised when an attepted to insert a duplicate record, is detected.
    """
    _record: Any
    _message: str

    def __init__(self,  record: Any, message: str):
        self._record = record
        self._message = message


    def __repr__(self) -> object:
        return f"message: {self._message} - record: {self._record}"



class MessageQueueError(ApplicationError):
    """
    Bass class for all message queue errors
    """
    pass


class TaskError(ApplicationError):
    """
    Base class for all task errors
    """
    pass
