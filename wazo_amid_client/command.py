# Copyright 2020-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import (
    AmidError,
    AmidProtocolError,
    AmidServiceUnavailable,
    InvalidAmidError,
)


class AmidCommand(RESTCommand):
    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise AmidServiceUnavailable(response)

        try:
            raise AmidError(response)
        except InvalidAmidError:
            RESTCommand.raise_from_response(response)

    @staticmethod
    def raise_from_protocol(response):
        try:
            raise AmidProtocolError(response)
        except InvalidAmidError:
            RESTCommand.raise_from_response(response)
