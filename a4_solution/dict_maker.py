"""This module provides a function for constructing a dictionary from
two lists; one of keys, the other of values.

Function:

    make_dict(key_list, values_list): Return a dict assembled with keys
        from key_list and corresponding values from values_list.

Author: R. Linley
Date: 2019-02-18
"""


def make_dict(key_list, values_list):
    """Return a dict assembled with keys from key_list and corresponding
    values from values_list.

    Parameters:
        key_list: A list containing keys for the new dictionary.

        values_list: A list of equal length to key_list containing
            values for the new dictionary.

    Return values:
        If key_list and value_list are the same length, a dictionary in
        which key_list[i] is a key paired with value values_list[i] for
        any i in range(len(key_list)).  Otherwise, returns None.
    """
    if len(key_list) != len(values_list):
        return None
    ret_dict = {}
    for i in range(len(key_list)):
        ret_dict[key_list[i]] = values_list[i]
    return ret_dict


if __name__ == "__main__":
    # Test code for module

    # Test for empty lists.
    print(make_dict([], []))  # {}

    # Test with lists of equal length.
    test_keys = ["Name", "Phone number", "Email address"]
    test_values = ["Baldwin, Alec", "613-357-3030",
                        "acj.baldwin@gmail.com"]
    test_dict = make_dict(test_keys, test_values)
    # test_dict should contain this dict:
    """
    {
        'Name': 'Baldwin, Alec',
        'Phone number': '613-357-3030',
        'Email address': 'acj.baldwin@gmail.com'
    }
    """
    print(test_dict)

    # Test that should return None (because of lists of unequal size):
    del test_values[2]  # Takes out the email address value
    print(make_dict(test_keys, test_values))  # None
