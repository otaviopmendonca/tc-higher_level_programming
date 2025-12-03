#!/usr/bin/python3
"""Singly linked list implementation with sorted insertion."""


class Node:
    """Represents a single node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a node with:
            - data: integer stored in the node
            - next_node: reference to the next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the integer value stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Validate and assign the node's data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return the next node linked to this node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node reference.
        Ensures the value is either None or another Node instance.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Manages a singly linked list with automatic sorted insertion."""

    def __init__(self):
        """Create an empty list with head set to None."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new node so that the list remains sorted in ascending order.
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a newline-separated string with all node values."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
