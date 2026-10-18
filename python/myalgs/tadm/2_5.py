#!/usr/bin/env python3


def asterisk(n: int) -> None:
    for k in range(1, n):
        x = k
        while x < n:
            print("*")
            x = 2 * x


if __name__ == "__main__":
    asterisk(4)
