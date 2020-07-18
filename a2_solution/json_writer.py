"""This module provides a function for writing data to a JSON
file.

Function:
    write_json_file(filename, data): Write data to JSON file, filename.

Author: R. Linley
Date: 2020-01-21

"""
import json


def write_json_file(filename, data):
    """Write data to JSON file, filename.

    Parameters:
        filename: The name of the file being created/overwritten. (As
            this is to be a JSON file, it's adviseable to end the
            filename with ".json".)

        data: Data of any type supported by JavaScript Object Notation
            (JSON). See https://www.geeksforgeeks.org/json-data-types/.

    Return values:
        If the write is successful, True, otherwise False.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except IOError:
        return False
    return True


if __name__ == "__main__":
    # Test code for module.
    import os  # This module has a remove() function for deleting files.

    # Here's a list containing a dict, two ints, and a list.
    test_data = [
        {"t1": "test1", "t2": "test2", "t3": "test3"},
        1111,
        2222,
        ["a", "b", "c"],
    ]
    test_filename = "testtesttest.json"
    if write_json_file(test_filename, test_data):
        print("Write to JSON file succeeded.")
    else:
        print("Write to JSON file failed.")
    # When read in again, the file content should look like this:
    """
    [
        {
            "t1": "test1",
            "t2": "test2",
            "t3": "test3"
        },
        1111,
        2222,
        [
            "a",
            "b",
            "c"
        ]
    ]
    """
    try:
        with open(test_filename, "r") as f:
            lines = f.read()
        print(lines)
        os.remove(test_filename)  # Get rid of the test file.
    except IOError:
        print("Something went wrong.")
