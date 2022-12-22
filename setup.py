#!/usr/bin/env python3
# Copyright 2014-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup
from setuptools import find_packages

setup(
    name='wazo_amid_client',
    version='1.0',
    description='a simple client library for the wazo-amid HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_amid_client.commands': [
            'action = wazo_amid_client.commands.action:ActionCommand',
            'command = wazo_amid_client.commands.command:CommandCommand',
            'status = wazo_amid_client.commands.status:StatusCommand',
        ],
    },
)
