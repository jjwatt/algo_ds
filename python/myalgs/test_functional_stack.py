import pytest

from functional_stack import (
    Cons,
    EmptyStackError,
    Nil,
    Stack,
    TupleStack,
    cons,
    to_list,
)


@pytest.fixture(params=[Nil, TupleStack])
def empty_stack[T](request: pytest.FixtureRequest) -> Stack[T]:
    """Parametrized fixture providing empty stacks of both implementations"""
    factory = request.param
    return factory()


def test_module_level_cons_basic() -> None:
    empty: Stack[int] = Nil()
    s = cons(1, cons(2, cons(3, empty)))

    assert not s.is_empty
    assert s.head() == 1
    assert s.tail().head() == 2
    assert s.tail().tail().head() == 3
    assert s.tail().tail().tail().is_empty


def test_module_level_cons_with_tuplestack() -> None:
    empty: Stack[str] = TupleStack()
    s = cons("world", cons("hello", empty))

    assert s.head() == "world"
    assert s.tail().head() == "hello"


def test_module_level_cons_structural_sharing() -> None:
    base: Stack[int] = cons(2, cons(1, Nil()))
    branch_a = cons(10, base)
    branch_b = cons(20, base)

    assert branch_a.tail() is base
    assert branch_b.tail() is base


def test_emtpy_stack_properties(empty_stack: Stack[int]) -> None:
    assert empty_stack.is_empty is True
    assert isinstance(empty_stack, Stack)


def test_empty_stack_errors(empty_stack: Stack[int]) -> None:
    with pytest.raises(EmptyStackError):
        empty_stack.head()

    with pytest.raises(EmptyStackError):
        empty_stack.tail()


def test_stack_immutability(empty_stack: Stack[str]) -> None:
    s0 = empty_stack
    s1 = cons("a", s0)
    s2 = cons("b", s1)

    assert s0.is_empty is True
    assert s1.head() == "a"
    assert s1.tail().is_empty == True
    assert s2.head() == "b"


def test_to_list(empty_stack: Stack[int]) -> None:
    s = cons(1, cons(2, cons(3, empty_stack)))
    assert to_list(s) == [1, 2, 3]


def test_to_list_empty(empty_stack: Stack[int]) -> None:
    assert to_list(empty_stack) == []

