def count_bits_naive(n: int) -> list[int]:
    ans = []
    for i in range(0, n + 1):
        count = 0
        for b in bin(i):
            if b == "1":
                count += 1
        ans.append(count)
    return ans


def count_bits(n: int) -> list[int]:
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


if __name__ == "__main__":
    input = 5
    output = count_bits(input)
    print(f"{output=}")
