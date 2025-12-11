#!/usr/bin/python3
"""
Task 0: Abstract Animal Class and its Subclasses
Demonstrates the use of ABCs to create an abstract Animal class
with an abstract method 'sound'
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class for all animals with the 'sound' method.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method representing the sound the animal makes.
        """
        pass

class Dog(Animal):
    """
    Subclass of Animal.
    Implements the abstract 'sound' method.
    """
    def sound(self):
        """
        Returns the sound a Dog makes.
        """
        return "Bark"

class Cat(Animal):
    """
    Subclass of Animal.
    Implements the abstract 'sound' method.
    """
    def sound(self):
        """
        Returns the sound a Cat makes.
        """
        return "Meow"
