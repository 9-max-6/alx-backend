#!/usr/bin/env python3
"""module: index_range"""
import csv
import math
from typing import List, Tuple, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """a function that takes page and page_size and returns the following:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        returned_dataset = self.get_page(page, page_size)
        length = math.ceil(len(self.__dataset)/page_size)
        return {
            "page_size": len(returned_dataset),
            "page": page,
            "data": returned_dataset,
            "next_page": None if page == length else page + 1,
            "prev_page": None if page == 1 else page - 1,
            "total_pages": length
        }


def index_range(page: int, page_size: int) -> Tuple:
    """params
    : page: page number
    : page_size: the size of the page
    """
    lower_index = 0
    for page in range(1, page):
        lower_index += page_size

    return (lower_index, lower_index + page_size)
