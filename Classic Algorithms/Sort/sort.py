"""
Problem
-------
**Sorting**
Implement two types of sorting
algorithms: Merge sort and bubble sort.


Solution
--------
Here follows two implementation of the
sorting algorithms merge sort and bubble
sort.

Author
------
dbonadiman

"""
import sys


def merge(l, r):
    """
    merge

    this function execute the merge step
    of the merge sort algorithm

    Parameters:
    l ==> the left list
    r ==> the right list

    Test:

    >>> merge([1, 5], [2, 3])
    [1, 2, 3, 5]

    >>> merge([1], [0])
    [0, 1]

    >>> merge([2], [])
    [2]

    >>> merge([], [3])
    [3]
    """
    res = []
    while l+r:
        if l and r:
            if l[0] < r[0]:
                res.append(l.pop(0))
            else:
                res.append(r.pop(0))
        elif l:
            res += l
            l = []
        elif r:
            res += r
            r = []
    return res


def merge_sort(lis):
    """
    merge_sort

    the merge sort algorithm recursively splits
    the list in small chunk (divide) and merging each
    small chunk creating an ordered , bigger one.

    Complexity:
    O(n log n) Worst case
    O(n log n) Average case

    Parameters:
    lis => the input-unordered list

    Test:

    >>> merge_sort([2, 4, 1, 7, 6, 4, 9, 0])
    [0, 1, 2, 4, 4, 6, 7, 9]

    >>> merge_sort([])
    []

    >>> merge_sort([0])
    [0]

    >>> merge_sort([2, 4, 1])
    [1, 2, 4]
    """
    if len(lis) < 2:
        return lis
    mid = int(len(lis)/2)
    left = merge_sort(lis[:mid])
    right = merge_sort(lis[mid:])
    return merge(left, right)


def bubble_sort(lis):
    """
    bubble_sort

    the bubble sort iterate over the list
    swapping ordering two near numbers.
    In a visual way it iterates over a list
    pushing each times the greater number to
    the end of the list

    Complexity:
    O(n^2) Worst case
    O(n^2) Average case
    O(n) Best case (ordered list)

    Parameters:
    lis => the input-unordered list

    Test:

    >>> bubble_sort([2, 4, 1, 7, 6, 4, 9, 0])
    [0, 1, 2, 4, 4, 6, 7, 9]

    >>> bubble_sort([])
    []

    >>> bubble_sort([0])
    [0]

    >>> bubble_sort([2, 4, 1])
    [1, 2, 4]
    """
    while True:
        n = len(lis)
        sw = False
        for j in range(n-1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
                sw = True
        n -= 1
        if not sw:
            break
    return lis


def main():
    try:
        print("\nThis program order lists using both bubble sort and\n"
              "merge sort."
              "Here follows the output on some lists.\n")

        lis = [2, 4, 1, 7, 6, 4, 9, 0]
        print("List: {}".format(lis))
        print("Merge Sorted list: {}".format(merge_sort(lis)))
        print("Bubble Sorted list: {}".format(bubble_sort(lis)))
        lis = []
        print("List: {}".format(lis))
        print("Merge Sorted list: {}".format(merge_sort(lis)))
        print("Bubble Sorted list: {}".format(bubble_sort(lis)))
        lis = [0]
        print("List: {}".format(lis))
        print("Merge Sorted list: {}".format(merge_sort(lis)))
        print("Bubble Sorted list: {}".format(bubble_sort(lis)))
        lis = [2, 4, 1]
        print("List: {}".format(lis))
        print("Merge Sorted list: {}".format(merge_sort(lis)))
        print("Bubble Sorted list: {}".format(bubble_sort(lis)))
        return 0
    except Exception, e:
        print(e)
        return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    status = main()
    sys.exit(status)
