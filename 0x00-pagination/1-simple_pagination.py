#!/usr/bin/env python3
"""module: index_range"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A function that implements pagination on a csv dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        first_index, last_index = index_range(page, page_size)
        try:
            return self.dataset()[first_index: last_index]
        except IndexError:
            return []


def index_range(page: int, page_size: int) -> Tuple:
    """params
    : page: page number
    : page_size: the size of the page
    """
    lower_index = 0
    for page in range(1, page):
        lower_index += page_size

    return (lower_index, lower_index + page_size)
