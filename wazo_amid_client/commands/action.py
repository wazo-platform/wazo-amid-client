# Copyright 2015-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_amid_client.command import AmidCommand


class ActionCommand(AmidCommand):

    resource = 'action'

    def __call__(self, action, params=None, **kwargs):
        url = f'{self.base_url}/{action}'
        r = self.session.post(url, json=params, params=kwargs)

        if r.status_code != 200:
            self.raise_from_response(r)

        results = r.json()
        for result in results:
            if result.get('Response') == 'Error':
                self.raise_from_protocol(r)

        return results
