# -*- coding: utf-8 -*-
# Copyright 2015-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.client import BaseClient


class AmidClient(BaseClient):

    namespace = 'wazo_amid_client.commands'

    def __init__(self, host, port=443, prefix='/api/amid', version='1.0', **kwargs):
        super(AmidClient, self).__init__(host=host, port=port, version=version, **kwargs)
