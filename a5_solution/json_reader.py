"""Module for reading a .json file into memory.

Function:

    read_json(filename): Return a dict of data extracted from file
        filename (a .json file).

Author: R. Linley
Date: 2020-03-11
"""
import json
import os


def read_json(filename):
    """Return a dict of data extracted from file filename
    (a .json file).
    """
    json_file = open(filename)
    return json.load(json_file)


if __name__ == "__main__":
    # Module testing.
    test = {"a": "apple", "b": "banana", "c": "cranberry",
            "d": ["date", "durian", "dragon fruit"]}
    test_filename = "test_test_test.json"
    with open(test_filename, "w") as test_file:
        json.dump(test, test_file)
    test_file.close()
    if test == read_json(test_filename):
        print("Test succeeded.")
    else:
        print("Test failed.")
    os.remove(test_filename)  # Delete test file.
    
    
