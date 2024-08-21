#!/usr/bin/env python3
"""LIFO Caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system with LIFO eviction policy"""
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache with LIFO eviction policy."""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_cache = self.order.pop(-1)
            del self.cache_data[last_cache]
            print(f"DISCARD: {last_cache}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
