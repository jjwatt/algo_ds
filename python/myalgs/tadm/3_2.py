#!/usr/bin/env python3
# *** 3-2
# Give an algorithm that takes a string $S$ consisting of opening and
# closing parentheses, say `)()(())()()))())))(`, and finds the length
# of the longest balanced parenthesis in $S$, which is 12 in the example
# above. (Hint: The solution is not necessarily a contiguous run of
# parenthesis from $S$).

import sys


def longest_balanced_subsequence_len(s: str) -> int:
    open_count = 0
    matched_pairs = 0

    for c in s:
        if c == "(":
            open_count += 1
        elif c == ")":
            if open_count > 0:
                matched_pairs += 1
                open_count -= 1
    return matched_pairs * 2


def longest_balanced_subsequence_len_stack(s: str) -> int:
    stack = []
    matched_pairs = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
                matched_pairs += 2
    return matched_pairs


if __name__ == "__main__":
    input = ")()(())()()))())))("
    output = longest_balanced_subsequence_len(input)

    print(f"{output=}")

    output2 = longest_balanced_subsequence_len_stack(input)
    print(f"{output2=}")

    if output2 == output:
        sys.exit(0)
    else:
        print(
            "Programming Error: Algorithms for balanced subsequence count don't match"
        )
        sys.exit(1)
