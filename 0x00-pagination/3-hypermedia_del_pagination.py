#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """A function to return a dataset and the description and solves the
        problem of offset pagination that occurs when a user makes
        consecutive queries with a database action of either
        addiiton or deletion
        """
        dataset_len = len(self.__dataset)
        assert index < dataset_len, "raised when out of range"
        next_index = page_size + index
        data = []
        if next_index >= dataset_len:
            #  Index out of range
            next_index = dataset_len
            page_size = dataset_len - index
        for i in range(index, next_index):
            data.append(self.indexed_dataset().get(i))

        data_dict = {
             'index': index,
             'data': data,
             'page_size': page_size if page_size != dataset_len else None,
             'next_index': next_index,
        }
        return data_dict
