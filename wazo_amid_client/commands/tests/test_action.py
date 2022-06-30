# -*- coding: utf-8 -*-
# Copyright 2014-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that
from hamcrest import equal_to

from wazo_lib_rest_client.tests.command import RESTCommandTestCase

from ..action import ActionCommand


class TestAction(RESTCommandTestCase):
    Command = ActionCommand

    def test_action_no_params(self):
        json_response = {'return': 'value'}
        self.session.post.return_value = self.new_response(
            200, json=[json_response]
        )

        result = self.command('QueueSummary')

        self.session.post.assert_called_once_with(
            f'{self.base_url}/QueueSummary', params={},
            json=None
        )
        assert_that(result, equal_to([json_response]))

    def test_action_with_params(self):
        json_response = {'return': 'value'}
        self.session.post.return_value = self.new_response(
            200, json=[json_response]
        )

        cmd = 'DBGet'
        params = {'Family': 'family', 'Key': 'key'}

        result = self.command(cmd, params)

        self.session.post.assert_called_once_with(
            f'{self.base_url}/{cmd}',
            params={},
            json=params,
        )
        assert_that(result, equal_to([json_response]))
