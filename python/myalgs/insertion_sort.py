from collections.abc import MutableSequence, Sequence
from typing import Protocol, Self


class SupportsLessThan(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...


class SupportsLessThanOrEqual(Protocol):
    def __le__(self, other: Self, /) -> bool: ...


class SupportsIndexSwap[T](Protocol):
    def __getitem__(self, index: int, /) -> T: ...
    def __setitem__(self, index: int, value: T, /) -> None: ...


class SupportsIndexableSort[T](Protocol):
    def __len__(self) -> int: ...
    def __getitem__(self, index: int, /) -> T: ...
    def __setitem__(self, index: int, value: T, /) -> None: ...


def insertion_sort1[T: SupportsLessThan](collection: SupportsIndexableSort[T]) -> None:
    """Insertion Sort from TheAlgorithms."""
    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        while (0 < insertion_index
               and  collection[insertion_index] < collection[insertion_index - 1]):
            collection[insertion_index], collection[insertion_index - 1] = (
                collection[insertion_index - 1],
                collection[insertion_index],
            )
            insertion_index = insertion_index - 1


def exchange[T](collection: SupportsIndexSwap[T], a: int, b: int) -> None:
    """Swap indexes a and b in collection."""
    collection[a], collection[b] = collection[b], collection[a]


# T has a BOUND (SupportsLessThan) while the container is PARAMETERIZED over T.
def insort[T: SupportsLessThan](collection: SupportsIndexableSort[T]) -> None:
    for i in range(1, len(collection)):
        j = i
        while (0 < j and collection[j] < collection[j - 1]):
            exchange(collection, j, (j-1))
            j -= 1


def insort_c[T: SupportsLessThan](collection: SupportsIndexableSort[T]) -> None:
    """Insertion sort ported from C."""
    for i in range(1, len(collection)):
        j = i - 1
        key = collection[i]
        while (0 <= j and key < collection[j]):
            collection[j + 1] = collection[j]
            j = j - 1
        collection[j + 1] = key


def insort_w(A: MutableSequence) -> MutableSequence:
    """Insertion sort from wikipedia and similar to the one from C.
    Wikipedia says that this is derived from expanding "swap" from the
    simpler definition.
    """
    i = 1
    while i < len(A):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = x
        i = i + 1
    return A


def finsert[T: SupportsLessThanOrEqual](lst: tuple[T, ...], x: T) -> tuple[T, ...]:
    """Inserts 'x' into sorted tuple 'lst' preserving sorted order."""
    match lst:
        case ():
            return (x,)
        case (y, *ys) if x <= y:
            return (x, y, *ys)
        case (y, *ys):
            return (y, *finsert(tuple(ys), x))
        case _:
            raise AssertionError("Unreachable")


def finsertion_sort[T: SupportsLessThanOrEqual](seq: Sequence[T]) -> tuple[T, ...]:
    """Sorts a sequence using functional insertion sort."""
    match tuple(seq):
        case ():
            return ()
        case (x, *xs):
            return finsert(finsertion_sort(tuple(xs)), x)
        case _:
            raise AssertionError("Unreachable")


