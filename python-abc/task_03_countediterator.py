#!/usr/bin/python3
"""
CountedIterator class that tracks the number of
items fetched during iteration.
"""

class CountedIterator:
    """
    Iterator wrapper that tracks how many items were returned.
    """

    def __init__(self, data):
        """
        Initialize with an iterable.
        """
        self.iterator = iter(data)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator.
        """
        return self

    def __next__(self):
        """
        Return next item and increment count.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        Return number of items iterated.
        """
        return self.count
