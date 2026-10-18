#!/usr/bin/env python3


def mystery(n: int) -> int:
    r = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            for k in range(1, j + 1):
                r += 1
    return r


if __name__ == "__main__":
    n = 0
    print(f"{n=}")
    print(f"{mystery(n)=}")

    n = 1
    print(f"{n=}")
    print(f"{mystery(n)=}")

    n = 2
    print(f"{n=}")
    print(f"{mystery(n)=}")

    n = 3
    print(f"{n=}")
    print(f"{mystery(n)=}")

    n = 4
    print(f"{n=}")
    print(f"{mystery(n)=}")

    n = 5
    print(f"{n=}")
    print(f"{mystery(n)=}")

    n = 6
    print(f"{n=}")
    print(f"{mystery(n)=}")
