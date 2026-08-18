from collections.abc import MutableSequence, Sequence
from typing import Protocol, Self


class SupportsLessThanOrEqual(Protocol):
    def __le__(self, other: Self, /) -> bool: ...


def insertion_sort1(collection: MutableSequence) -> MutableSequence:
    """Insertion Sort from TheAlgorithms."""
    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        while (insertion_index > 0
               and collection[insertion_index - 1] > collection[insertion_index]):
            collection[insertion_index], collection[insertion_index - 1] = (
                collection[insertion_index - 1],
                collection[insertion_index],
            )
            insertion_index = insertion_index - 1
    return collection


def exchange(collection: MutableSequence, a: int, b: int) -> None:
    """Swap indexes a and b in collection."""
    collection[a], collection[b] = collection[b], collection[a]


def dec(num: int) -> int:
    """Return an int one less than num."""
    return num - 1


def insort(collection: MutableSequence) -> MutableSequence:
    for i in range(1, len(collection)):
        j = i
        while (j > 0 and collection[j - 1] > collection[j]):
            exchange(collection, j, (j-1))
            j = dec(j)
    return collection

def insort_c(collection: MutableSequence) -> MutableSequence:
    """Insertion sort ported from C."""
    for i, _ in enumerate(collection):
        j = i - 1
        key = collection[i]
        while (j >= 0 and key < collection[j]):
            collection[j + 1] = collection[j]
            j = j - 1
        collection[j + 1] = key
    return collection

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


def finsertion_sort[T: SupportsLessThanOrEqual](seq: Sequence[T]) -> tuple[T, ...]:
    """Sorts a sequence using functional insertion sort."""
    match tuple(seq):
        case ():
            return ()
        case (x, *xs):
            return finsert(finsertion_sort(tuple(xs)), x)


