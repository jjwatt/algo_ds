import random


myrandom10list = random.choices(range(1, 50), k=10)
def compsort(junk):
    """From taocp-vol3.1e p76.
    Algorithm C: Sorting by Counting.
    ((compare Kj with Ki) for 1 <= j <= i) for 1 < i <= N.
    where K is keys and i and j are indexes.
    COUNT[j] tells us where to move Rj
    Args:
      junk: A list of comparables.
    Returns:
      count: "count[j] tells us where to move junk[j]"
             "The invers of the permutation p(1)...p(n) is
             specified in the COUNT table.
    """
    # Set COUNT[1] through COUNT[N] to 0.
    # Knuth is using 1-based index.
    N = len(junk) - 1
    count = [0 for i in junk]
    i = N
    while i >= 1:
        j = i - 1
        while j >= 0:
            # print("i, j: ", i, j)
            if junk[i] < junk[j]:
                # print("count[j] = count[j] + 1")
                # print("j = ", j)
                count[j] = count[j] + 1
                # print("count[j] = ", count[j])
            else:
                # print("count[i] = count[i] + 1")
                # print("i  ", i)
                count[i] = count[i] + 1
                # print("count[i] = ", count[i])
            # print("dec j, j = ", j-1)
            j = j - 1
        # print("dec i, i = ", i-1)
        i = i - 1
    return count
def pycompsort(junk):
    """A more pythonic version with the same spirit."""
    count = [0 for i in junk]
    for i, value in enumerate(junk):
        for j in range(i - 1, -1, -1):
            if junk[j] > value:
                count[j] = count[j] + 1
            else:
                count[i] = count[i] + 1
    return count

def sortwithtable(junk, count_table):
    """Use the count table to sort the junk list."""
    newjunk = [0 for i in junk]
    for i, j in enumerate(count_table):
        newjunk[j] = junk[i]
    return newjunk

def insertion_sort(L):
    """A normal insertion sort.
    Mutates the argument. No return.
    """
    #TODO(jjwatt): Better naming. Algorithm examples are bad code :P
    for i in range(1, len(L)):
        j = i - 1
        key = L[i]
        while(L[j] > key) and (j >= 0):
            L[j+1] = L[j]
            j = j - 1
        L[j+1] = key


def mymerge(left, right):
    """Recursive merge, the way I would do it in scheme.

    Look how clean this reads. Right?
    Pretty slow in Python, though.
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] > right[0]:
        return [right[0]] + mymerge(left, right[1:])
    else:
        return [left[0]] + mymerge(left[1:], right)


def take(l, n):
    if not n:
        return list()
    else:
        return [l[0]] + take(l[1:], n - 1)


def mymergesort(alist):
    """Recursive mergesort, the way I'd do it in scheme."""
    if len(alist) < 2:
        return alist
    split = len(alist) // 2
    left  = alist[:split]
    right = alist[split:]
    return mymerge(mymergesort(left), mymergesort(right))


def createlist(n, rng=None):
    if rng is None:
        rng = (1, 255)
    return random.choices(range(*rng), k=n)


def swap(val1, val2):
    val1, val2 = val2, val1


class bubblesort(object):
    def my_in_place(self, arr):
        """My off-the-cuff in place bubblesort based on English description."""
        for _, item in enumerate(arr):
            for idx2 in range(len(arr) - 1):
                if arr[idx2] > arr[idx2 + 1]:
                    arr[idx2], arr[idx2 + 1] = arr[idx2 + 1], arr[idx2]
    def myprr(self, arr, acc):
        """Partial recursive in-place bubblesort."""
        if acc == 1:
            # Base case
            return arr
        i = 0
        while i < acc - 1:
            if arr[i] > arr[i+1]:
                swap(arr[i], arr[i+1])
            i += 1
        self.mypr(arr, acc - 1)
    def fr_bubble_sort(self, arr):
        """Fully recursive bubblesort.

        Still messy. This is like bubble_up and
        schemey_bubble_sort, but all put together
        to 'hide' the aux functions. Still no loops!
        """
        def _bsort(ar2):
            """All the 'hard work' in this fn."""
            if ar2[1:] == []:
                return ar2
            if ar2[0] > ar2[1]:
                return [ar2[1]] + _bsort([ar2[0]] + ar2[2:])
            else:
                return [ar2[0]] + _bsort(ar2[1:])
        def _dec(counter, ar1):
            """Helper fn to track counter and call _bsort."""
            if counter == 1:
                return _bsort(ar1)
            else:
                return _dec(counter - 1, _bsort(ar1))
        return _dec(len(arr), arr)
    def bubble_up(self, arr):
        """Recursive bubbler.

        Use this with aux methods to bubble up values.
        """
        if arr[1:] == []:
            return arr
        if arr[0] < arr[1]:
            return [arr[0]] + self.bubble_up(arr[1:])
        else:
            return [arr[1]] + self.bubble_up([arr[0]] + arr[2:])
    def bubble_sort_aux(self, counter, arr):
        if counter == 1:
            return self.bubble_up(arr)
        else:
            return self.bubble_sort_aux(counter - 1, self.bubble_up(arr))
    def schemey_bubble_sort(self, arr):
        counter = len(arr)
        return self.bubble_sort_aux(counter, arr)



