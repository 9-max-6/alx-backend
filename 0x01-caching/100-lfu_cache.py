#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A class to implement the least frequently
    used cache replacement policy"""

    def __init__(self):
        """init"""
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """A function to add a key-value pair to
        the cache
        """
        dic_keys = self.cache_data.keys()
        if key and item:
            if len(dic_keys) == self.MAX_ITEMS:
                index = self.drop_lfu()
                del self.cache_data[index]
                print(f"DISCARD: {index}")

            self.cache_data[key] = item
            self.used_keys.append(key)

    def get(self, key):
        """A function to get a value when passed
        a key
        """
        if key:
            value = self.cache_data.get(key)
            if value:
                self.used_keys.append(key)
            return value

    def drop_lfu(self):
        """a function to determine lfu index"""
        lfu = ""
        count = len(self.cache_data)
        for key in reversed(self.used_keys):
            cur_count = self.used_keys.count(key)
            if cur_count <= count:
                lfu = key
                count = cur_count

        while lfu in self.used_keys:
            self.used_keys.remove(lfu)
        return lfu
