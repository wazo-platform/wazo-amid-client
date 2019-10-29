# -*- coding: utf-8 -*-
# Copyright 2016-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import RESTCommand


class CommandCommand(RESTCommand):

    resource = 'action'

    def __call__(self, command):
        body = {'command': command}
        url = '{base}/Command'.format(base=self.base_url)
        r = self.session.post(url, json=body)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
