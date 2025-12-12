#!/usr/bin/python3
"""
VerboseListn class that extends list and prints
notifications when items are added or removed.
"""


class VerboseList(list):
    """
    List subclass that prints notifications when elements
    are added or removed.
    """

    def append(self, item):
        """
        Appends an 'item' to the list and prints a
        confirmation message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extends the list with elements from an iterable and notificates
        """
        items_added = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """
        Remove item from list with notification
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop item from list and notificates
        """
        item = self[index] if self else None
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
