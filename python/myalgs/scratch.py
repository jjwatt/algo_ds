

#TODO: Use Python Typing/type hints
#TODO: Organize better with stuff in algo_ds/python/myalgs/sorting.py

def insertion_sort1(collection):
    """Insertion Sort from TheAlgorithms."""
    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        breakpoint()
        while (insertion_index > 0
               and collection[insertion_index - 1] > collection[insertion_index]):
            collection[insertion_index], collection[insertion_index - 1] = (
                collection[insertion_index - 1],
                collection[insertion_index],
            )
            breakpoint()
            insertion_index = insertion_index - 1
            breakpoint()
    breakpoint()
    return collection

def insort(collection):
    for i in range(1, len(collection)):
        j = i
        while (j > 0 and collection[j - 1] > collection[j]):
            exchange(collection, j, (j-1))
            j = dec(j)
        breakpoint()
    breakpoint()
    return collection

def insort_c(collection):
    for i, _ in enumerate(collection):
        j = i - 1
        key = collection[i]
        breakpoint()
        while (j >= 0 and key < collection[j]):
            collection[j + 1] = collection[j]
            j = j - 1
            breakpoint()
        collection[j + 1] = key
        breakpoint()
    return collection


def insort_w(A):
    """Insortion sort from wikipedia and similar to the one from C.
    Wikipedia says that this is derived from expanding "swap" from them
    simpler definition.
    """
    i = 1
    while i < len(A):
        x = A[i]
        j = i - 1
        breakpoint()
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = x
        i = i + 1
    return A


def exchange(collection, a, b):
    collection[a], collection[b] = collection[b], collection[a]


def dec(num):
    return num - 1


# Reverse in-place
def reverse_in_place(col):
    start = 0
    end = len(col) - 1
    while start < end:
        col[start], col[end] = col[end], col[start]
        start += 1
        end -= 1
