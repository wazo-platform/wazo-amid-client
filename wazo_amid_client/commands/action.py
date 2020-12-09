# -*- coding: utf-8 -*-
# Copyright 2015-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_amid_client.command import AmidCommand


class ActionCommand(AmidCommand):

    resource = 'action'

    def __call__(self, action, params=None, **kwargs):
        url = '{base}/{action}'.format(base=self.base_url, action=action)
        r = self.session.post(url, json=params, params=kwargs)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
