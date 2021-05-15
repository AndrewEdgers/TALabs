import time

from numpy import random

blessRNG100K = random.randint(100500, size=100000)
q1K = blessRNG100K.copy()
m1K = blessRNG100K.copy()
s1K = blessRNG100K.copy()
h1K = blessRNG100K.copy()
blessRNG1M = random.randint(1000500, size=1000000)
q1M = blessRNG1M.copy()
m1M = blessRNG1M.copy()
s1M = blessRNG1M.copy()
h1M = blessRNG1M.copy()
pogChamp100K = [x for x in range(0, 100000)]
q2K = pogChamp100K.copy()
m2K = pogChamp100K.copy()
s2K = pogChamp100K.copy()
h2K = pogChamp100K.copy()
pogChamp1M = [x for x in range(0, 1000000)]
q2M = pogChamp1M.copy()
m2M = pogChamp1M.copy()
s2M = pogChamp1M.copy()
h2M = pogChamp1M.copy()

"""
def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)"""


def choose_pivot(arr, lo, hi):
    return arr[hi]


def partition(arr, lo, hi, pivot):
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def quicksort(arr, lo, hi):
    if lo < hi:
        pivot = choose_pivot(arr, lo, hi)
        pos = partition(arr, lo, hi, pivot)
        quicksort(arr, lo, pos - 1)
        quicksort(arr, pos + 1, hi)


def mergesort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergesort(L)

        # Sorting the second half
        mergesort(R)

        i = j = k = 0

        # Copy item to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def shellsort(array):
    sublistcount = len(array) // 2
    while sublistcount > 0:
        for start_position in range(sublistcount):
            gapInsertionSort(array, start_position, sublistcount)
        sublistcount = sublistcount // 2


def gapInsertionSort(array, start, gap):
    for i in range(start + gap, len(array), gap):

        current_value = array[i]
        position = i

        while position >= gap and array[position - gap] > current_value:
            array[position] = array[position - gap]
            position = position - gap

        array[position] = current_value


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    # maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def main():
    """start_time = time.time()
    quicksort(q1K, 0, len(q1K) - 1)
    print("--- Quicksort 100K Random: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    quicksort(q1M, 0, len(q1M) - 1)
    print("--- Quicksort 1M Random: %s seconds ---" % (time.time() - start_time))
"""
    start_time = time.time()
    quicksort(q2K, 0, len(q2K) - 1)
    print("--- Quicksort 100K Sorted: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    quicksort(q2M, 0, len(q2M) - 1)
    print("--- Quicksort 1M Sorted: %s seconds ---" % (time.time() - start_time))
    print("---------------------------------------")

    start_time = time.time()
    mergesort(m1K)
    print("--- Merge sort 100K Random: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    mergesort(m1M)
    print("--- Merge sort 1M Random: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    mergesort(m2K)
    print("--- Merge sort 100K Sorted: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    mergesort(m2M)
    print("--- Merge sort 1M Sorted: %s seconds ---" % (time.time() - start_time))
    print("---------------------------------------")

    start_time = time.time()
    shellsort(s1K)
    print("--- Shell sort 100K Random: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    shellsort(s1M)
    print("--- Shell sort 1M Random: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    shellsort(s2K)
    print("--- Shell sort 100K Sorted: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    shellsort(s2M)
    print("--- Shell sort 1M Sorted: %s seconds ---" % (time.time() - start_time))
    print("---------------------------------------")

    start_time = time.time()
    heapsort(h1K)
    print("--- Heap sort 100K Random: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    heapsort(h1M)
    print("--- Heap sort 1M Random: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    heapsort(h2K)
    print("--- Heap sort 100K Sorted: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    heapsort(h2M)
    print("--- Heap sort 1M Sorted: %s seconds ---" % (time.time() - start_time))
    print("=======================================")


if __name__ == '__main__':
    main()
