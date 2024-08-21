#!/usr/bin/env python3
"""LRU Caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A caching system with LRU eviction policy"""
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache with LRU eviction policy."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_recently_used = self.order.pop(0)
                del self.cache_data[least_recently_used]
                print(f"DISCARD: {least_recently_used}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache by key."""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
