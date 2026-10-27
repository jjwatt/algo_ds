#!/usr/bin/env python3
# *** 3-1
# A common problem for compilers and text editors is determining whether
# a parantheses in a string are balanced and properly nested. For
# example, the string =((())())()= contains properly nested pairs of
# praentheses, while the strings =)()(= and =())= do not. Give an
# algorithm that returns true if a string contains properly nested and
# balanced parentheses, and false if otherwise. For full credit,
# identify the position of the first offending parenthesis if the string
# is not properly nested and balanced.

import sys


def check_balanced_parentheses(s: str) -> tuple[bool, int | None]:
    stack: list[int] = []

    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if not stack:
                return False, i
            stack.pop()
    if stack:
        # If there are still items in the stack, there are unclosed parens.
        # First offending open paren is the earliest in the stack.
        return False, stack[0]

    return True, None


if __name__ == "__main__":
    tests: list[tuple[str, tuple[bool, int | None]]] = [
        ("((())())()", (True, None)),
        (")()(", (False, 0)),
        ("())", (False, 2)),
        ("((())", (False, 0)),
    ]

    for test_input, want in tests:
        got = check_balanced_parentheses(test_input)
        passing = want[0]
        if got == want:
            print(f"Successfully marked parens {'passing' if passing else 'failing'}")
        else:
            print(
                f"Programming Error: Algorithm failed to mark parens {'passing' if passing else 'failing'}"
            )
            sys.exit(1)
