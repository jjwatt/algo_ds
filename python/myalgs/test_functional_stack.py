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

