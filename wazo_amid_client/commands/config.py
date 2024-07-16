# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_amid_client.command import AmidCommand

from ..types import JSON


class ConfigCommand(AmidCommand):
    resource = 'config'

    def __call__(self):
        headers = self._get_headers()
        url = self.base_url
        r = self.session.get(url, headers=headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def patch(self, config_patch: dict[str, JSON]) -> JSON:
        headers = self._get_headers()
        r = self.session.patch(self.base_url, headers=headers, json=config_patch)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
