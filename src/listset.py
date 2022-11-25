"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        ...  # FIXME
        self.data = list()
        for x in init:
            self.add(x)
    #Running time = kvadratisk/O(n^2) --> self.data er konstant O(1), for er lineær O(n), og self.add er lineær O(n), det giver derfor O(n^2)

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        ...  # FIXME
        return x in self.data
    #kigger hele listen igennem/laver en lineær search og derfor Running time = lineær/O(n)

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        ...  # FIXME
        return bool(self.data)
    #bool-funktionen har Running time = konstant/O(1)

    def __str__(self) -> str:
        """ ~ Pretty print ~ """
        return str(self.data)
    #str-frunktion har Running time = lineær/O(n)

    def add(self, x: T) -> None:
        """Add x to the set."""
        ...  # FIXME
        if x not in self.data:
            self.data.append(x)
    #not in-funktionen lineær search mens append har konstant kompleksitet, altså Running time = lineær/O(n)

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        ...  # FIXME
        if x in self.data:
            self.data.remove(x)
    #Running time lineær/O(n) --> Searching har Running time O(n), Remove har Running time O(n) og de skal lægges sammen og ikke ganges.