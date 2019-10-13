# -*- coding: utf-8 -*-
# Copyright (C) 2015 Avencall
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client.client import BaseClient


class AmidClient(BaseClient):

    namespace = 'amid_client.commands'

    def __init__(self, host, port=9491, version='1.0', **kwargs):
        super(AmidClient, self).__init__(host=host, port=port, version=version, **kwargs)
