#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class to implement FIFO caching"""
    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """A function to add a key to the cache dictionary"""
        if key and item:
            self.cache_data[key] = item

        dic_keys = self.cache_data.keys()
        if len(dic_keys) > self.MAX_ITEMS:
            del_key = list(dic_keys)[0]
            del self.cache_data[del_key]
            print(f"DISCARD: {del_key}")

    def get(self, key):
        """A function to get a """
        if key:
            return self.cache_data.get(key)
