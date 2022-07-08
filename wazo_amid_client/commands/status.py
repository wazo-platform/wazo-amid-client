# -*- coding: utf-8 -*-
# Copyright 2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_amid_client.command import AmidCommand


class StatusCommand(AmidCommand):
    resource = 'status'

    def __call__(self):
        headers = self._get_headers()
        url = self.base_url
        r = self.session.get(url, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
