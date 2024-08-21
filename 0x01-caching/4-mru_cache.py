#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """a function to implement the least recently used
    cache replacement policy"""

    def __init__(self):
        """init"""
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """A function to add an item to the cache"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.update_mru(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    mru_key = self.mru()
                    del self.cache_data[mru_key]
                    print(f"DISCARD: {mru_key}")

                self.cache_data[key] = item
                self.update_mru(key)

    def mru(self):
        """A function to determine the key with the
        least count"""
        mru_index = self.used_keys.pop(-1)
        return mru_index

    def update_mru(self, key):
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
            self.update_mru(key)
            return self.cache_data.get(key)
        return None
