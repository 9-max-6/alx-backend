#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")


class LIFOCache(BaseCaching):
    """A class to implement the LIFO cache"""
    def __init__(self):
        """Initialize"""
        super().__init__()
    
    def put(self, key, item):
        """A function to add an item to the cache"""
        dic_keys = self.cache_data.keys()

        if dic_keys == self.MAX_ITEMS:
            del_key = dic_keys[-1]
            del self.cache_data[del_key]
            print(f"DISCARD: {del_key}")

        if key and item:
            self.cache_data[key] = item
    
    def get(self, key):
        """A function to get a """
        if key:
            return self.cache_data.get(key)
