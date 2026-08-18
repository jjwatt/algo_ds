"""Tests for insertion sorts."""
from insertion_sort import insertion_sort1


def test_insertion_sort1() -> None:
    col = list(range(10, 0, -1))
    assert col[0] == 10
    insertion_sort1(col)
    assert col[0] == 1


