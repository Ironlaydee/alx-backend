#!/usr/bin/evn python3
'''A function that defines class Server that paginates a database of popular baby names
'''

import csv
from typing import list, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' From a given page, collect the index range'''

    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)


class Server:
    ''' Server class to paginate a database of popular baby names'''

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        ''' Cached dataset'''

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Collect a page of dataset'''

        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
