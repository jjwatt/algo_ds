#!/usr/bin/env python3


def remove_k_digits(num: str, k: int) -> str:
    stack: list[str] = []

    for digit in num:
        # Maintain a monotonic increasing order in the stack.
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # If k is still greater than 0, remove the largest remaining digits from the tail.
    if k > 0:
        stack = stack[:-k]

    # Strip leading zeros and handle the empty string case.
    result = "".join(stack).lstrip("0")

    return result if result else "0"


if __name__ == "__main__":
    num = "1432219"
    k = 3
    output = remove_k_digits(num, k)
    print(f"{output=}")
