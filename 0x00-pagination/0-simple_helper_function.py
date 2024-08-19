#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Simple helper function to calculate start and end indices"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
