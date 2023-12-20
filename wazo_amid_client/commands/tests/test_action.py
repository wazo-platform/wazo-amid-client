# Copyright 2014-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that, equal_to
from wazo_lib_rest_client.tests.command import RESTCommandTestCase

from ..action import ActionCommand


class TestAction(RESTCommandTestCase):
    Command = ActionCommand

    def test_action_no_params(self):
        self.session.post.return_value = self.new_response(
            200, json=[{'return': 'value'}]
        )

        result = self.command('QueueSummary')

        self.session.post.assert_called_once_with(
            f'{self.base_url}/QueueSummary', params={}, json=None
        )
        assert_that(result, equal_to([{'return': 'value'}]))

    def test_action_with_params(self):
        self.session.post.return_value = self.new_response(
            200, json=[{'return': 'value'}]
        )

        result = self.command('DBGet', {'Family': 'family', 'Key': 'key'})

        self.session.post.assert_called_once_with(
            f'{self.base_url}/DBGet',
            params={},
            json={'Family': 'family', 'Key': 'key'},
        )
        assert_that(result, equal_to([{'return': 'value'}]))
