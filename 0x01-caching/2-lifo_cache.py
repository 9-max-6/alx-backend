#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class to implement the LIFO cache"""
    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """A function to add an item to the cache"""
        dic_keys = self.cache_data.keys()

        if len(dic_keys) == self.MAX_ITEMS:
            del_key = list(dic_keys)[-1]
            del self.cache_data[del_key]
            print(f"DISCARD: {del_key}")

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """A function to get a """
        if key:
            return self.cache_data.get(key)
