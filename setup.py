#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2014-2015 Avencall
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup
from setuptools import find_packages

setup(
    name='xivo_amid_client',
    version='1.0',

    description='a simple client library for the xivo-amid HTTP interface',

    author='Wazo Authors',
    author_email='dev.wazo@gmail.com',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'amid_client.commands': [
            'action = xivo_amid_client.commands.action:ActionCommand',
            'command = xivo_amid_client.commands.command:CommandCommand',
        ],
    }
)
