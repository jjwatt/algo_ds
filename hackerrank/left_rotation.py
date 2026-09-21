# A operation on a circular array shifts each of the array's elements
# unit to the left. The elements that fall off the left end reappear at
# the right end. Given an integer , rotate the array that many steps to
# the left and return the result.


def rotate_left(a: list[int], d: int) -> list[int]:
    n = len(a)
    d = d % n
    return a[d:] + a[:d]


# In-place O(1) Space ("The Three Reversals" Trick)
def rotate_left_inplace(a: list[int], d: int) -> list[int]:
    n = len(a)
    d = d % n
    if d == 0:
        return a

    def reverse_range(arr: list[int], left: int, right: int) -> None:
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Reverse the first d elements: [0, d - 1].
    reverse_range(a, 0, d - 1)
    # Reverse the rest: [d, n - 1].
    reverse_range(a, d, n - 1)
    # Reverse the entire array: [0, n - 1].
    reverse_range(a, 0, n - 1)

    return a


if __name__ == "__main__":
    input = [1, 2, 3, 4, 5]
    print("Using rotate_left")
    print(f"{input=}")
    output = rotate_left(input, 4)
    print(f"{output=}")

    print("Using rotate_left_inplace")
    print(f"{input=}")
    rotate_left_inplace(input, 4)
    print(f"{input=}")
