# Copyright 2016-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_amid_client.command import AmidCommand


class CommandCommand(AmidCommand):

    resource = 'action'

    def __call__(self, command):
        body = {'command': command}
        url = f'{self.base_url}/Command'
        r = self.session.post(url, json=body)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
