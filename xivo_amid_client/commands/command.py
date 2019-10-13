# -*- coding: utf-8 -*-
# Copyright (C) 2016 Avencall
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client import RESTCommand


class CommandCommand(RESTCommand):

    resource = 'action'

    def __call__(self, command):
        body = {'command': command}
        url = '{base}/Command'.format(base=self.base_url)
        r = self.session.post(url, json=body)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
