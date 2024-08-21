#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """a function to implement the least recently used
    cache replacement policy"""

    def __init__(self):
        """init"""
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """A function to add an item to the cache"""
        if key and item:
            dic_keys = self.cache_data.keys()
            if len(dic_keys) == self.MAX_ITEMS:
                del_key = self.lru()
                del self.cache_data[del_key]
                print(f"DISCARD: {del_key}")

            self.cache_data[key] = item
            self.update_lru(key)

    def lru(self):
        """A function to determine the key with the
        least count"""
        lru_index = self.used_keys.pop(0)
        return lru_index

    def update_lru(self, key):
        """A function to update used_keys"""
        if key not in self.used_keys:
            self.used_keys.append(key)
        else:
            self.used_keys.remove(key)
            self.used_keys.append(key)

    def get(self, key):
        """A function to return the value in self.cache_data
        linked to key"""
        if key in self.cache_data:
            self.update_lru(key)
            return self.cache_data.get(key)
        return None
