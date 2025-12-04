# Copyright 2024-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from typing import TypeAlias

JSON: TypeAlias = str | int | float | bool | None | list['JSON'] | dict[str, 'JSON']
