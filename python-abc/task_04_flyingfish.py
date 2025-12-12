#!/usr/bin/python3
"""
Simple class examples for inheritance and method overriding.
"""

class Fish:
    """
    Represents a fish.
    """
    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat info."""
        print("The fish lives in water")


class Bird:
    """
    Represents a bird.
    """
    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat info."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A fish that can glide.
    """
    def fly(self):
        """Print flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print habitat info."""
        print("The flying fish lives both in water and the sky!")
