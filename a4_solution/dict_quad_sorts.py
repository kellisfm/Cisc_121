"""
Module to enable quadratic sorting of long dictionaries.

Functions:
insertion_sort(a_list_dict, key): Insertion sorts list of dictionaries, a_list_dict,
in ascending order by the values of key, key.

bubble_sort(a_list_dict, key): Bubble sorts list of dictionaries, a_list_dict,
in ascending order by the values of key, key.

bubble_sort_opt(a_list_dict, key): Optimally bubble sorts list of dictionaries, a_list_dict,
in ascending order by the values of key, key.

selection_sort(a_list_dict, key): Selection sorts list of dictionaries, a_list_dict,
in ascending order by the values of key, key.

Academic integrety note: code was taken from course slides and modidified to correctly function on 
lists of dicts

Author: K. Ellis
Section: 002
Student number: 20019803
Date: 2020-03-03
"""


def insertion_sort(a_list_dict, key):
    """Insertion sorts list of dictionaries, a_list_dict,
     in ascending order by the values of key, key."""
    i = 1
    for i in range(1, len(a_list_dict)):
        j = i
        while j > 0 and a_list_dict[j - 1][key] > a_list_dict[j][f"{key}"]:
            a_list_dict[j], a_list_dict[j - 1] = a_list_dict[j -
                                                             1], a_list_dict[j]
            j -= 1


def bubble_sort(a_list_dict, key):
    """Bubble sorts list of dictionaries, a_list_dict,
     in ascending order by the values of key, key."""
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(a_list_dict)):
            if a_list_dict[i - 1][f"{key}"] > a_list_dict[i][f"{key}"]:
                a_list_dict[i -
                            1], a_list_dict[i] = a_list_dict[i], a_list_dict[i
                                                                             -
                                                                             1]
                swapped = True


def bubble_sort_opt(a_list_dict, key):
    "Optimally bubble sorts list of dictionaries, a_list_dict, in ascending order by the values of key, key."
    n = len(a_list_dict)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if a_list_dict[i - 1][f"{key}"] > a_list_dict[i][f"{key}"]:
                a_list_dict[i -
                            1], a_list_dict[i] = a_list_dict[i], a_list_dict[i
                                                                             -
                                                                             1]
            n -= 1


def selection_sort(a_list_dict, key):
    """Selection sorts list of dictionaries, a_list_dict, in ascending order by the values of key, key."""
    n = len(a_list_dict)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a_list_dict[j][f"{key}"] < a_list_dict[min][f"{key}"]:
                min = j
        if min != i:
            a_list_dict[i], a_list_dict[min] = a_list_dict[min], a_list_dict[i]


if __name__ == "__main__":

    tstlistdict = []
    tstlistdict.append({'fs': 'b', 'fi': 4, 'ff': 1.1})
    tstlistdict.append({'fs': 'c', 'fi': 6, 'ff': 1.2})
    tstlistdict.append({'fs': 'd', 'fi': 8, 'ff': 3.3})
    tstlistdict.append({'fs': 'a', 'fi': 1, 'ff': 3.3})
    tstlistdict.append({'fs': 'aaaa', 'fi': 5, 'ff': 3.3})

    insertion_sort(tstlistdict, "fs")  #fs:a, aaaa, b, c, d
    print(tstlistdict)
    t = insertion_sort(tstlistdict, "fi")  #fi: 1, 3, 5, 6, 8
    print(tstlistdict)
    t = insertion_sort(tstlistdict, "ff")  # ff: 1.1, 1.2, 3.3, 3.3, 3.3, 3.3
    print(tstlistdict)