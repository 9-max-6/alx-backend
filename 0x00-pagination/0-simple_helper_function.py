#!/usr/bin/env python3
"""module: index_range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """params
    : page: page number
    : page_size: the size of the page
    """
    lower_index = 0
    for page in range(1, page):
        lower_index += page_size

    return (lower_index, lower_index + page_size)
