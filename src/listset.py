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
        self.data = init
    #Running time = lineær/O(n)?

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        ...  # FIXME
        if x in self.data:
            return True
        else:
            return False
    #in-funktionen laver en lineær search og derfor Running time = lineær/O(n)

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        ...  # FIXME
        return bool(self)
    #bool-funktionen har Running time = konstant/O(1)?

    def add(self, x: T) -> None:
        """Add x to the set."""
        ...  # FIXME
        if x not in self:
            self.data.append(x)
    #not in-funktionen lineær search mens append har konstant kompleksitet, altså Running time = lineær/O(n)?

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        ...  # FIXME
        if x in self:
            idx = self.data.index(x)
            self.data.pop(idx)
    #in-funktioner laver lineær search, og pop-funktionen skal rykke alle elementer efter idx, så Running time = kvadratisk/O(n^2)?
