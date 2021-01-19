# -*- coding: utf-8 -*-
# Copyright 2020-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from requests import HTTPError


class AmidError(HTTPError):
    def __init__(self, response):
        try:
            body = response.json()
        except ValueError:
            raise InvalidAmidError()

        self.status_code = response.status_code
        try:
            self.message = body['message']
            self.error_id = body['error_id']
            self.details = body['details']
            self.timestamp = body['timestamp']
            if body.get('resource', None):
                self.resource = body['resource']
        except KeyError:
            raise InvalidAmidError()

        exception_message = '{e.message}: {e.details}'.format(e=self)
        super(AmidError, self).__init__(exception_message, response=response)


class AmidServiceUnavailable(AmidError):
    pass


class AmidProtocolError(AmidError):
    def __init__(self, response):
        try:
            body = response.json()
        except ValueError:
            raise InvalidAmidError()

        try:
            for msg in body:
                self.message = msg['Message']
        except (TypeError, KeyError):
            raise InvalidAmidError()

        exception_message = '{e.message}'.format(e=self)
        super(HTTPError, self).__init__(exception_message, response=response)


class InvalidAmidError(Exception):
    pass
