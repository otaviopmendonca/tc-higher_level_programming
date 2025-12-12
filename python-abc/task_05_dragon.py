#!/usr/bin/python3
"""
Mixin examples and a Dragon class.
"""


class SwimMixin:
    """Provides swimming behavior."""
    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying behavior."""
    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A creature that can swim, fly, and roar."""
    def roar(self):
        """Print roaring action."""
        print("The dragon roars!")
