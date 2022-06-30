# -*- coding: utf-8 -*-
# Copyright 2016-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that
from hamcrest import equal_to

from wazo_lib_rest_client.tests.command import RESTCommandTestCase

from ..command import CommandCommand


class TestCommand(RESTCommandTestCase):
    Command = CommandCommand

    def test_command(self):
        json_response = {'return': 'value'}
        self.session.post.return_value = self.new_response(
            200, json=json_response
        )

        asterisk_command = 'core show channels'
        result = self.command(asterisk_command)

        self.session.post.assert_called_once_with(
            f'{self.base_url}/Command',
            json={'command': asterisk_command},
        )
        assert_that(result, equal_to(json_response))
