#!/usr/bin/env python3


def prev_smaller(arr: list[int]) -> list[int]:
    n = len(arr)
    ans = [-1] * n
    stack: list[int] = []

    for i, val in enumerate(arr):
        # Pop candidates that cannot be smaller than current
        # and cannot be useful to anyone to the right.
        while stack and stack[-1] >= val:
            stack.pop()
        # If candidates remain, the top is our nearest smaller.
        if stack:
            ans[i] = stack[-1]

        # Add current element as a viable candidate for elements to the right.
        stack.append(val)

    return ans


if __name__ == "__main__":
    input = [4, 5, 2, 10, 8]
    print(f"{input=}")
    output = prev_smaller(input)
    print(f"{output=}")
