# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Utilities for explicit search tag normalization."""

from __future__ import annotations

from typing import Iterable, List


def normalize_search_tags(tags: Iterable[str] | None) -> List[str]:
    """Normalize explicit search tags while preserving user intent."""
    if not tags:
        return []

    normalized: List[str] = []
    seen: set[str] = set()
    for item in tags:
        if item is None:
            continue
        value = str(item).strip().lower()
        if not value or value in seen:
            continue
        seen.add(value)
        normalized.append(value)
    return normalized
