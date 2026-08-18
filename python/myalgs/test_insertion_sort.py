"""Tests for insertion sorts."""
from insertion_sort import insertion_sort1, finsert, finsertion_sort


def test_insertion_sort1() -> None:
    col = list(range(10, 0, -1))
    assert col[0] == 10
    insertion_sort1(col)
    assert col[0] == 1


def test_finsert() -> None:
    col_t = tuple(range(1, 11))
    assert col_t[0] == 1
    res_t = finsert(col_t, 11)
    assert res_t[0] == 1
    assert res_t[-1] == 11


def test_finsertion_sort() -> None:
    col = list(range(10, 0, -1))
    assert col[0] == 10
    res = finsertion_sort(col)
    assert res[0] == 1

