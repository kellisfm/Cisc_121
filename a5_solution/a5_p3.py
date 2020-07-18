"""This is a solution to part 3 of CISC 121 Winter 2020 Assignment 5, Gnome sort.

Functions:

    sort(a):  Sort list a into ascending order by value.
        (a) a list class object

Author: K. ellis
SN: 20019803
Section: 002
Date: 2020-04-01
"""
from random import randint


def sort(a, pos=0):
    """Sort list a into ascending order by value.
    Adapted from https://en.wikipedia.org/wiki/Gnome_sort#Code.
    """
    if pos < len(a):
        if pos == 0 or a[pos] >= a[pos - 1]:
            pos += 1
            sort(a, pos)
        else:
            a[pos], a[pos - 1] = a[pos - 1], a[pos]
            pos -= 1
            sort(a, pos)


if __name__ == "__main__":
    # Module testing.

    # sort
    # Empty list (should have no effect)
    test = []
    sort(test)
    print(test)  # []

    # One-item list (should have no effect)
    test = [0]
    sort(test)
    print(test)  # [0]

    # Two-item lists (ascending, equal, and descending values)
    test = [0, 1]
    sort(test)
    print(test)  # [0, 1]
    test = [1, 0]
    sort(test)
    print(test)  # [0, 1]
    test = [0, 0]
    sort(test)
    print(test)  # [0, 0]

    # Three-item lists (ascending, mixed, and descending values)
    test = [0, 1, 2]
    sort(test)
    print(test)  # [0, 1, 2]
    test = [0, 2, 1]
    sort(test)
    print(test)  # [0, 1, 2]
    test = [2, 0, 1]
    sort(test)
    print(test)  # [0, 1, 2]
    test = [2, 1, 0]
    sort(test)
    print(test)  # [0, 1, 2]

    # Larger, randomized list
    test = [randint(0, 100) for i in range(10)]
    print(test)
    test1 = test
    sort(test1)
    print(test1)  # list with values in ascending order
    gsort(test)
    print(test)
