# -*- coding: utf-8 -*-
# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import AmidError
from .exceptions import AmidServiceUnavailable
from .exceptions import InvalidAmidError


class AmidCommand(RESTCommand):

    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise AmidServiceUnavailable(response)

        try:
            raise AmidError(response)
        except InvalidAmidError:
            RESTCommand.raise_from_response(response)
