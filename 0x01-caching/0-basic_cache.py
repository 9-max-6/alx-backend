#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A caching system that inherits from the
    BaseCaching class
    """
    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """A function to add an item to the cache"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """A function to return the value linked to the key"""
        if key:
            return self.cache_data.get(key)
