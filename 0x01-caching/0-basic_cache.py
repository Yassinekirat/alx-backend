#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system with no limit"""

    def put(self, key, item):
        """Add an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
