"""
This is a solution to part 1 of the CISC 121 Winter 2020 Assignment 5.

Function:

    fubar(n,x,y): a mathematical function that can only be programmed through recursion

Author: K. ellis
SN: 20019803
Section: 002
Date: 2020-04-01
"""


def fubar(n, x, y):
    if n == 0:
        return x + y
    elif y == 0:
        return x
    else:
        return fubar(n - 1, fubar(n, x, y - 1), fubar(n, x, y - 1) + y)


if __name__ == "__main__":
    # Module testing for fubar.
    results = []
    for n in range(2):
        results.append([])
        for y in range(15):
            results[n].append([])
            for x in range(15):
                results[n][y].append(fubar(n, x, y))
    for page in results:
        for row in page:
            print("".join(f"{e:7}" for e in row))
        print()