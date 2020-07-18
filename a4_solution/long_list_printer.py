"""Module to assist with abbreviated printing of long lists.

Function:

    print_list(a_list, section_size): Print entire list a_list if its
    length is less than or equal to 3 times section_size (an int).
    Otherwise, print the first, middle, and last section_size elements
    only.

Author: R. Linley
Modified by: Kai Ellis
Section: 002
Student number: 20019803
Date: 2020-02-16
"""
import math


def print_list(a_list, section_size):
    """Print entire list a_list if its length is less than or equal to
    3 times section_size (an int).  Otherwise, print the first
    section_size elements of a_list, followed by an ellipsis ("...")
    followed by the middle section_size elements, followed by another
    ellipsis, followed by the final section_size elements.

    Note: This function assumes its parameters' values are valid, and
    does no exception handling.
    """
    ss3 = section_size * 3
    len_list = len(a_list)
    ss = (len(a_list) // 2) - math.floor(section_size / 2)
    es = (len(a_list) // 2) + math.ceil(section_size / 2)

    if len_list <= ss3:
        print(a_list)
    elif section_size == 0:
        print(a_list)
    else:
        print(a_list[:section_size], "...", a_list[ss:es], "...",
              a_list[-section_size:])


if __name__ == "__main__":
    # Module testing.

    # Tests with empty list.
    a = []
    print_list(a, 0)  # <no output>
    print_list(a, 1)  # <no output>
    print_list(a, 2)  # <no output>

    # Tests with lists of length <= section size
    a = ["This", "is", "a", "test"]
    print_list(a, 0)  # No sectioning
    print()

    print_list(a, 1)  # Three sections, "is" omitted.
    # ("is" omitted because of way partitioning into sections is done.)
    print()

    print_list(a, 2)  # No sectioning
    print()

    # Test with a longer list.
    # Here I'm using a technique called list comprehension to generate
    # a list of integers from 0 ... 99. This is beyond the scope of
    # CISC 121 (that is, it won't be on a test), but is useful if you
    # can get to know how it works.
    a = [i for i in range(100)]
    print_list(a, 5)
    # 0...4, "...", 48...52, "...", 95...99
    print()

    print_list(a, 10)
    # 0...9, "...", 45...54, "...", 90...99
    print()

    print_list(a, 33)
    # 0...32, "...", 34...66, "...", 67...99 (33 omitted)
    print()

    print_list(a, 34)
    # 0...99 (no sectioning)
    print()

    # Test with a list of a length evenly divisible by 3 and a
    # section size that is 1/3 of that.
    a = [i for i in range(33)]  # a is now length 33.
    print_list(a, 11)
    # 0...32 (no sectioning)

    # Test with demo list from Assignment 4.
    a = [
        [93, 80, 99, 72, 86, 84, 85, 41, 69, 31],
        [15, 37, 58, 59, 98, 40, 63, 84, 87, 15],
        [48, 50, 43, 68, 69, 43, 46, 83, 11, 50],
        [52, 49, 87, 77, 39, 21, 84, 13, 27, 82],
        [64, 49, 12, 42, 24, 54, 43, 69, 62, 44],
        [54, 90, 67, 43, 72, 17, 22, 83, 28, 68],
        [18, 12, 10, 73, 81, 40, 56, 33, 37, 19],
        [81, 72, 88, 92, 76, 21, 25, 20, 23, 58],
        [28, 79, 33, 22, 16, 66, 35, 84, 74, 55],
        [21, 46, 75, 21, 52, 74, 79, 91, 42, 20],
        [63, 37, 67, 48, 14, 91, 47, 87, 83, 34],
        [70, 85, 28, 19, 40, 50, 23, 23, 70, 11],
        [58, 89, 69, 43, 56, 30, 99, 27, 11, 32],
        [70, 34, 33, 41, 49, 47, 72, 92, 45, 29],
        [71, 85, 90, 31, 98, 74, 13, 83, 20, 49],
        [56, 46, 76, 66, 93, 19, 56, 71, 16, 77],
        [12, 22, 71, 71, 90, 44, 97, 18, 51, 29],
        [66, 96, 64, 67, 12, 71, 29, 78, 13, 27],
        [31, 71, 56, 22, 40, 13, 46, 81, 34, 51],
        [83, 10, 26, 56, 34, 24, 51, 65, 27, 70],
    ]
    print_list(a, 3)
